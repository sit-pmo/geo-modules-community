#!/usr/bin/env python3
"""Génère les pages de docs/modules/ depuis les dépôts GitHub des modules.

Pour chaque module de scripts/modules.json, lit dans son dépôt public :
  - src/plugin.geoext.json : nom affiché, version, version minimale de GEO ;
  - README.md              : page de présentation ;
  - CHANGELOG.md           : journal des nouveautés (facultatif) ;
  - GUIDE-DEV.md           : guide de développement (facultatif).

Seule la bibliothèque standard est utilisée. Le dossier docs/modules/ est régénéré à chaque exécution et
n'est pas versionné. Une erreur sur un fichier obligatoire arrête le script : mieux vaut ne rien publier
qu'un site à moitié construit.
"""
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "docs" / "modules"
CONFIG = json.loads((ROOT / "scripts" / "modules.json").read_text(encoding="utf-8"))
ORG = CONFIG["organisation"]
BRANCH = CONFIG["branche"]

# Fichiers du dépôt qui deviennent des pages du site : les liens qui les visent restent internes
INTERNAL_PAGES = {"CHANGELOG.md": "changelog.md", "GUIDE-DEV.md": "guide-dev.md", "README.md": "index.md"}


def fetch(repo, path, required=True):
    url = f"https://raw.githubusercontent.com/{ORG}/{repo}/{BRANCH}/{path}"
    try:
        with urllib.request.urlopen(url, timeout=30) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        if error.code == 404 and not required:
            return None
        sys.exit(f"Échec de lecture de {url} : HTTP {error.code}")
    except urllib.error.URLError as error:
        sys.exit(f"Échec de lecture de {url} : {error.reason}")


def rewrite_links(markdown, repo):
    """Rend absolus les liens et images relatifs du dépôt, hors blocs de code."""
    blob = f"https://github.com/{ORG}/{repo}/blob/{BRANCH}/"
    raw = f"https://raw.githubusercontent.com/{ORG}/{repo}/{BRANCH}/"

    def is_relative(target):
        return not re.match(r"^([a-z][a-z0-9+.-]*:|#|/)", target, re.I)

    def fix(match):
        bang, label, target = match.group(1), match.group(2), match.group(3).strip()
        if not is_relative(target):
            return match.group(0)
        path, _, anchor = target.partition("#")
        path = path[2:] if path.startswith("./") else path
        if not bang and path in INTERNAL_PAGES:
            return f"[{label}]({INTERNAL_PAGES[path]}{'#' + anchor if anchor else ''})"
        base = raw if bang else blob
        return f"{bang}[{label}]({base}{path}{'#' + anchor if anchor else ''})"

    def fix_html(match):
        target = match.group(2)
        return match.group(0) if not is_relative(target) else f'{match.group(1)}"{raw}{target}"'

    lines, in_fence = [], False
    for line in markdown.splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
        elif not in_fence:
            line = re.sub(r"(!?)\[([^\]]*)\]\(([^)\s]+)\)", fix, line)
            line = re.sub(r'(src=)"([^"]+)"', fix_html, line)
        lines.append(line)
    return "\n".join(lines) + "\n"


def drop_title(markdown):
    """Retire le premier titre de niveau 1 : le titre de la page vient de la fiche du module."""
    return re.sub(r"\A\s*# .*\n", "", markdown, count=1).lstrip("\n")


def first_paragraph(markdown):
    for block in re.split(r"\n\s*\n", drop_title(markdown)):
        text = block.strip()
        if text and not text.startswith(("#", ">", "|", "```", "-", "!", "<")):
            return re.sub(r"\s+", " ", text)
    return ""


def build_module(entry):
    repo, slug = entry["repo"], entry["slug"]
    manifest = json.loads(fetch(repo, "src/plugin.geoext.json"))
    readme = fetch(repo, "README.md")
    changelog = fetch(repo, "CHANGELOG.md", required=False)
    guide = fetch(repo, "GUIDE-DEV.md", required=False)

    name = manifest.get("displayName", slug)
    version = manifest.get("version", "?")
    min_geo = manifest.get("minGeoVersion", "?")
    repo_url = f"https://github.com/{ORG}/{repo}"
    summary = manifest.get("description") or first_paragraph(readme)

    folder = OUT / slug
    folder.mkdir(parents=True, exist_ok=True)

    header = (
        f"# {name}\n\n"
        f'!!! info "Version {version}"\n'
        f"    Module GEO **{manifest.get('name', slug)}** · compatible GEO **{min_geo}** et suivants · "
        f"licence GPL-3.0-or-later\n\n"
        f"    [:lucide-download: Télécharger le ZIP]({repo_url}/releases/latest){{ .md-button .md-button--primary }} "
        f"[:lucide-github: Dépôt]({repo_url}){{ .md-button }} "
        f"[:lucide-bug: Signaler un problème]({repo_url}/issues){{ .md-button }}\n\n"
        f"Pour installer le ZIP, voir [Installer un module](../../installer.md).\n\n"
    )
    (folder / "index.md").write_text(header + rewrite_links(drop_title(readme), repo), encoding="utf-8")

    if changelog:
        body = "# Journal des nouveautés — " + name + "\n\n" + rewrite_links(drop_title(changelog), repo)
        (folder / "changelog.md").write_text(body, encoding="utf-8")
    if guide:
        body = "# Guide de développement — " + name + "\n\n" + rewrite_links(drop_title(guide), repo)
        (folder / "guide-dev.md").write_text(body, encoding="utf-8")

    pages = ["index.md"] + [f for f in ("changelog.md", "guide-dev.md") if (folder / f).exists()]
    return {"slug": slug, "name": name, "version": version, "summary": summary, "min_geo": min_geo, "pages": pages}


def write_index(modules):
    rows = "\n".join(
        f"| [{m['name']}]({m['slug']}/index.md) | {m['version']} | {m['min_geo']} | "
        f"{m['summary'][:220].replace('|', '/')} |"
        for m in modules
    )
    page = (
        "# Les modules\n\n"
        "Modules d'extension pour la plateforme GEO de Business Geografic, publiés sous licence GPL-3.0-or-later.\n\n"
        "| Module | Version | GEO minimum | Description |\n|---|---|---|---|\n" + rows + "\n\n"
        "Pour importer un module dans votre application : [Installer un module](../installer.md).\n"
    )
    (OUT / "index.md").write_text(page, encoding="utf-8")


def update_nav(modules):
    """Réécrit, dans zensical.toml, la zone de navigation comprise entre les marqueurs « modules »."""
    config = ROOT / "zensical.toml"
    text = config.read_text(encoding="utf-8")
    entries = []
    for m in modules:
        title = m["name"].replace("\\", "\\\\").replace('"', '\\"')
        pages = ", ".join(f'"modules/{m["slug"]}/{page}"' for page in m["pages"])
        entries.append(f'    {{ "{title}" = [ {pages} ] }},')
    block = "\n".join(["    # >>> modules"] + entries + ["    # <<< modules"])
    new, count = re.subn(r"^ *# >>> modules\n.*?^ *# <<< modules", lambda _: block, text, flags=re.S | re.M)
    if count != 1:
        sys.exit("Marqueurs « # >>> modules » / « # <<< modules » introuvables dans zensical.toml")
    if new != text:
        config.write_text(new, encoding="utf-8")


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)
    modules = [build_module(entry) for entry in CONFIG["modules"]]
    modules.sort(key=lambda m: m["slug"])
    write_index(modules)
    update_nav(modules)
    print(f"{len(modules)} modules : " + ", ".join(f"{m['slug']} {m['version']}" for m in modules))


if __name__ == "__main__":
    main()
