# geo-modules-community

Site de documentation des [modules d'extension GEO](https://vienne-condrieu-agglomeration.github.io/geo-modules-community/) de Vienne Condrieu
Agglomération : catalogue, installation, retours d'expérience de développement et contribution.

Le site est construit avec [Zensical](https://zensical.org/) et publié par GitHub Pages.

## Structure

```
docs/                    Pages écrites à la main : accueil, installer, contribuer, developper/
docs/modules/            Pages de chaque module : GÉNÉRÉES (non versionnées)
scripts/modules.json     Liste des modules affichés
scripts/collect_modules.py   Lit le dépôt de chaque module (fiche, README, CHANGELOG, GUIDE-DEV) et génère docs/modules/
zensical.toml            Configuration du site
requirements.txt         Version de Zensical (figée)
.github/workflows/docs.yml   Construction et déploiement
```

## Travailler en local

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
python scripts/collect_modules.py     # génère docs/modules/ (accès réseau à GitHub)
zensical serve                        # http://localhost:8000
```

## Ajouter un module au site

Ajouter une entrée `{ "repo": "geo-module-<nom>", "slug": "<nom>" }` dans `scripts/modules.json`. Le dépôt du module doit être public et contenir
`src/plugin.geoext.json` et `README.md` ; `CHANGELOG.md` et `GUIDE-DEV.md` sont repris s'ils existent.

## Mettre à jour le site

Chaque push sur `main` reconstruit et publie le site. Une reconstruction manuelle (onglet *Actions*, « Run workflow ») reprend la dernière version
publiée de chaque module. Réglage requis une fois : *Settings > Pages > Source : GitHub Actions*.

## Licence

Contenu sous [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), code des scripts sous GPL-3.0-or-later.
