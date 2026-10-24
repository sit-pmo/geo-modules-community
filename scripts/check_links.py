#!/usr/bin/env python3
"""Contrôle les liens du site construit (dossier site/ par défaut).

  - liens internes et ancres : doivent exister dans le site → erreur sinon ;
  - liens externes : « mort » (HTTP 404/410, nom de domaine introuvable) → erreur ;
    autres échecs (403, 429, délai dépassé, certificat) → avertissement seulement, car ils sont souvent passagers
    ou propres au poste qui teste.

Code de sortie : 1 s'il y a une erreur, 0 sinon (les avertissements ne bloquent pas).
Usage : zensical build --clean && python scripts/check_links.py [dossier-du-site]
Seule la bibliothèque standard est utilisée.
"""
import concurrent.futures as cf
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "site").resolve()
SITE_URL = re.search(r'^site_url\s*=\s*"([^"]+)"', (ROOT / "zensical.toml").read_text(encoding="utf-8"), re.M).group(1)
if not SITE_URL.endswith("/"):
    SITE_URL += "/"

_ids = {}


def ids_of(page):
    if page not in _ids:
        text = page.read_text(encoding="utf-8", errors="replace")
        _ids[page] = set(re.findall(r'\b(?:id|name)="([^"]+)"', text))
    return _ids[page]


def collect():
    """Parcourt les pages : renvoie (liens internes cassés, ancres cassées, liens externes → pages source)."""
    broken, bad_anchors, external = [], [], {}
    for page in sorted(SITE.rglob("*.html")):
        rel = page.relative_to(SITE).as_posix()
        url = SITE_URL + (rel[: -len("index.html")] if rel.endswith("index.html") else rel)
        html = page.read_text(encoding="utf-8", errors="replace")
        for href in sorted(set(re.findall(r'<a\b[^>]*?\bhref="([^"]*)"', html))):
            if href.startswith(("mailto:", "tel:", "javascript:")):
                continue
            full = urllib.parse.urljoin(url, href)
            parsed = urllib.parse.urlparse(full)
            if full.startswith(SITE_URL):
                path = urllib.parse.unquote(full[len(SITE_URL):].split("#")[0].split("?")[0])
                candidates = [SITE / path, SITE / path / "index.html"] if path else [SITE / "index.html"]
                target = next((c for c in candidates if c.is_file()), None)
                if target is None:
                    broken.append((rel, href))
                elif parsed.fragment and target.suffix == ".html" and parsed.fragment not in ids_of(target):
                    bad_anchors.append((rel, href))
            elif parsed.scheme in ("http", "https"):
                external.setdefault(full.split("#")[0], set()).add(rel)
    return broken, bad_anchors, external


def probe(link):
    """Renvoie (lien, 'ok' | 'mort' | 'avertissement', détail)."""
    headers = {"User-Agent": "Mozilla/5.0 (geo-modules-community link check)"}
    detail = "?"
    for method in ("HEAD", "GET"):
        try:
            request = urllib.request.Request(link, method=method, headers=headers)
            with urllib.request.urlopen(request, timeout=20):
                return link, "ok", ""
        except urllib.error.HTTPError as error:
            detail = f"HTTP {error.code}"
            if error.code in (404, 410):
                return link, "mort", detail
            if method == "HEAD":
                continue   # certains serveurs refusent HEAD : on retente en GET
        except urllib.error.URLError as error:
            detail = str(error.reason)
            if isinstance(error.reason, socket.gaierror):
                return link, "mort", "nom de domaine introuvable"
            if method == "HEAD":
                continue
        except Exception as error:   # délai dépassé, connexion coupée…
            detail = type(error).__name__
            if method == "HEAD":
                continue
    return link, "avertissement", detail


def main():
    if not SITE.is_dir():
        sys.exit(f"Dossier introuvable : {SITE} (lancer d'abord « zensical build --clean »)")
    broken, bad_anchors, external = collect()
    with cf.ThreadPoolExecutor(8) as pool:
        results = list(pool.map(probe, sorted(external)))
    dead = [r for r in results if r[1] == "mort"]
    warnings = [r for r in results if r[1] == "avertissement"]

    pages = len(list(SITE.rglob("*.html")))
    print(f"{pages} pages · {len(external)} liens externes uniques · internes cassés : {len(broken)} · "
          f"ancres cassées : {len(bad_anchors)} · externes morts : {len(dead)} · avertissements : {len(warnings)}")
    for page, href in broken:
        print(f"ERREUR  lien interne cassé   {page} → {href}")
    for page, href in bad_anchors:
        print(f"ERREUR  ancre introuvable    {page} → {href}")
    for link, _, detail in dead:
        print(f"ERREUR  lien externe mort    {detail} : {link}  (dans {', '.join(sorted(external[link])[:2])})")
    for link, _, detail in warnings:
        print(f"AVERT.  lien externe douteux {detail} : {link}")
    sys.exit(1 if broken or bad_anchors or dead else 0)


if __name__ == "__main__":
    main()
