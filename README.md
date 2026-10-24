# geo-modules-community

Site de documentation des [modules d'extension GEO](https://vienne-condrieu-agglomeration.github.io/geo-modules-community/) de Vienne Condrieu
Agglomération : catalogue, installation, retours d'expérience de développement et contribution.

Le site est construit avec [Zensical](https://zensical.org/) et publié par GitHub Pages.

## Structure

```
docs/                    Pages écrites à la main : accueil, installer, contribuer, gouvernance, developper/
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
zensical serve                        # http://localhost:8000 (utiliser le Zensical du .venv : la version est figée)
```

Contrôler les liens du site construit :

```bash
zensical build --clean
python scripts/check_links.py         # code de sortie 1 en cas de lien interne ou externe mort
```

## Ajouter un module au site

Ajouter une entrée `{ "repo": "geo-module-<nom>", "slug": "<nom>" }` dans `scripts/modules.json`. Le dépôt du module doit être public et contenir
`src/plugin.geoext.json` et `README.md` ; `CHANGELOG.md` et `GUIDE-DEV.md` sont repris s'ils existent.

## Le script de collecte (`scripts/collect_modules.py`)

Il génère les pages « modules » du site à partir des dépôts GitHub des modules. Il tourne avant `zensical build`, en local comme dans le workflow.
Il n'utilise que la bibliothèque standard de Python.

1. Lit `scripts/modules.json` (dépôts, slugs, organisation, branche).
2. Récupère pour chaque module, sur `raw.githubusercontent.com` : `src/plugin.geoext.json` et `README.md` (obligatoires), `CHANGELOG.md` et
   `GUIDE-DEV.md` (facultatifs).
3. Écrit dans `docs/modules/<slug>/` : `index.md` (en-tête avec version, GEO minimum, licence et boutons ZIP / dépôt / issues, puis le README),
   `changelog.md` et `guide-dev.md` s'ils existent.
4. Réécrit les liens du README : liens vers `CHANGELOG.md` et `GUIDE-DEV.md` rendus internes au site, autres liens et images relatifs rendus absolus
   vers le dépôt. Les blocs de code ne sont pas modifiés.
5. Génère `docs/modules/index.md`, le tableau des modules (description réduite à du texte brut, coupée à la dernière phrase entière).
6. Met à jour le `nav` de `zensical.toml`, **uniquement** entre les marqueurs `# >>> modules` et `# <<< modules`.

À savoir :

- `docs/modules/` est **effacé et recréé** à chaque exécution et n'est pas versionné : ne jamais l'éditer à la main.
- Le script s'arrête au moindre échec sur un fichier obligatoire (dépôt introuvable, erreur réseau) : mieux vaut ne rien publier qu'un site à moitié construit.
- Il modifie `zensical.toml` (zone entre les marqueurs) : après l'ajout d'un module, ce fichier apparaît dans `git diff` et doit être commité.
- Il lit la branche indiquée dans `modules.json` (`main`), c'est-à-dire le dernier état poussé, pas la dernière release.

## Mettre à jour le site

- **Déploiement** : chaque push sur `main` reconstruit et publie le site.
- **Demandes de fusion** : le site est construit sans être déployé (`check.yml`), pour détecter une erreur avant la fusion.
- **Pages des modules** : le workflow les régénère chaque lundi, et à la demande (onglet *Actions*, « Run workflow »). Elles reprennent le dernier
  état de la branche `main` de chaque module.
- **Liens** : `links.yml` construit le site et lance `scripts/check_links.py` chaque lundi ; un lien interne ou externe mort fait échouer le
  workflow, ce qui prévient par mail.
- **Dépendances** : Dependabot ouvre chaque mois une demande de fusion groupée pour Zensical et pour les actions GitHub, assignée à `allfab` ; la
  construction en PR vérifie qu'elles passent.
- Réglage requis une fois : *Settings > Pages > Source : GitHub Actions*.

## Licence

Contenu sous [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/deed.fr), code des scripts sous GPL-3.0-or-later.
