---
icon: lucide/database
---

# Données et intégrateurs

Certains modules ont besoin de données qu'aucun service GEO ne fournit. Plutôt que d'exiger un serveur ou une base de données, la bibliothèque
publie ces données sous forme de **fichiers statiques** (JSON), préparés à partir d'une source ouverte par un **intégrateur** : un petit programme
Python (bibliothèque standard, sans dépendance) qui télécharge la source, la contrôle et la convertit. Le module les lit directement dans le
navigateur : pas de serveur, pas de base de données, aucun mot de passe.

!!! note "Projets indépendants"
    Les intégrateurs et leurs données sont des projets communautaires, **non affiliés à Business Geografic** ni à l'administration qui produit la
    source. GEO est un produit de Business Geografic.

## Comment ça fonctionne

Chaque famille de données a **deux dépôts** :

| Dépôt | Rôle |
|---|---|
| `geo-community-integrator-<nom>` | Le code de l'intégrateur, versionné (une version = un tag). Sa documentation décrit le format des fichiers produits : c'est le contrat avec le module. |
| `geo-community-data-<nom>` | Un workflow GitHub Actions qui lance l'intégrateur et publie le résultat sur GitHub Pages. Il vérifie chaque semaine si la source a changé et ne republie que si c'est le cas. |

Le **format de sortie** porte un numéro de version (`format` dans `index.json`). Un module refuse un format qu'il ne connaît pas et demande sa
mise à jour, au lieu d'afficher des résultats faux. Les champs ajoutés sans casser l'existant (par exemple le nom des communes) ne changent pas ce
numéro.

## Filiation des parcelles (DFI)

Alimente le module [Filiation des parcelles](modules/dfi/index.md) : l'historique des divisions, réunions, lotissements et remaniements de chaque
parcelle cadastrale, d'après les **Documents de filiation informatisés** de la DGFiP.

- **Source** : [DFI des parcelles](https://www.data.gouv.fr/datasets/documents-de-filiation-informatises-dfi-des-parcelles) sur data.gouv.fr, publiés
  chaque trimestre sous **Licence Ouverte 2.0**. Le module affiche la source et la date de mise à jour, comme la licence l'exige.
- **Intégrateur** : [geo-community-integrator-dfi](https://github.com/vienne-condrieu-agglomeration/geo-community-integrator-dfi) (GPL-3.0-or-later).
  Il produit un fichier JSON par commune et un `index.json` qui porte le nom des communes (API Géo) et la date de la situation. Il sait traiter un
  ou plusieurs départements, ou toute la France (environ 1,5 Go de JSON pour 34 900 communes, converties en cinq minutes).
- **Données** : [geo-community-data-dfi](https://github.com/vienne-condrieu-agglomeration/geo-community-data-dfi), publiées sur GitHub Pages.
  Les départements publiés sont réglés par une variable du dépôt (`DFI_DEPARTMENTS`).

### Utiliser vos propres données

Le module lit par défaut les données publiées par la bibliothèque. Une collectivité qui veut d'autres départements, ou ses propres données, peut
**publier les siennes** : le module accepte une autre adresse (réglage « Adresse des données » dans le Générateur). Deux possibilités :

1. Copier le dépôt `geo-community-data-dfi` (fork), régler sa variable `DFI_DEPARTMENTS` et activer GitHub Pages (source : GitHub Actions) ;
2. Lancer l'intégrateur sur un poste et déposer le dossier produit sur n'importe quel serveur web qui répond en **HTTPS** avec l'en-tête
   `Access-Control-Allow-Origin` (sans cela, le navigateur bloque la lecture depuis GEO).

!!! warning "Limite de GitHub Pages"
    Un site GitHub Pages ne dépasse pas **1 Go**. Toute la France (1,5 Go) n'y tient donc pas : choisissez vos départements, ou un autre hébergement.

## Proposer un intégrateur

Un nouvel intégrateur suit la même convention : un dossier de code et un dépôt de données, une version de format de sortie, une licence de la
source citée dans les données. Voir [Contribuer](contribuer.md) pour proposer l'idée avant d'écrire du code.
