---
icon: lucide/users
---

# Gouvernance

Cette page décrit comment la bibliothèque est animée : qui décide, comment une idée devient une fonctionnalité, et comment les contributions sont
reprises et publiées.

!!! warning "Version de travail"
    Cette page est une **proposition soumise à discussion**. Les valeurs marquées *(à valider)* sont des suggestions, pas des engagements.
    Les remarques sont les bienvenues sur le [Discord du Club Utilisateurs GEO](contribuer.md#echanger-avec-la-communaute) ou dans une
    [issue](https://github.com/vienne-condrieu-agglomeration/geo-modules-community/issues).

## Principes

- **Ouvert** : le code est sous GPL-3.0-or-later, la documentation sous CC-BY-4.0, et chacun peut proposer des changements.
- **Utile avant tout** : un module doit résoudre un besoin réel et fonctionner dans un GEO réel. Une idée se juge à son usage.
- **Transparent** : les décisions sont écrites là où tout le monde peut les lire, avec leur raison, y compris quand la réponse est « non ».
- **Simple** : peu de règles, des modèles et des listes de contrôle plutôt que des procédures.

## Rôles

| Rôle | Qui | Ce que le rôle permet |
|---|---|---|
| **Mainteneur** | Le service SIG et Foncier de Vienne Condrieu Agglomération | Décide de l'intégration, fusionne, publie les versions |
| **Co-mainteneur** | Un contributeur actif invité par les mainteneurs, pour un ou plusieurs modules *(à valider)* | Relit et fusionne des contributions sur ses modules |
| **Contributeur** | Toute personne qui signale un problème, propose une idée ou une modification | Ouvre des issues et des demandes de fusion |
| **Utilisateur** | Toute personne qui installe un module | Signale les problèmes, partage ses retours |

Un contributeur régulier peut être invité comme co-mainteneur ; la décision se prend entre mainteneurs, avec son accord.

## De l'idée à la fonctionnalité

1. **Échanger** (facultatif) : une idée peut d'abord se discuter sur le [Discord](contribuer.md#echanger-avec-la-communaute) pour mesurer
   l'intérêt.
2. **Proposer** : ouvrir une *issue* sur le dépôt du module, avec le modèle « Proposer une fonctionnalité » : le besoin, l'usage concret, la
   version de GEO concernée. **Le Discord ne remplace pas l'issue** : seule l'issue garde la trace de la décision.
3. **Discuter** : les mainteneurs et la communauté commentent. Les mainteneurs précisent si la proposition entre dans le périmètre du module.
4. **Décider** : les mainteneurs tranchent après un délai de discussion *(à valider : environ deux semaines)* et l'indiquent dans l'issue par un
   label :
    - `acceptée` : la fonctionnalité est retenue, avec son porteur (qui la développe) ;
    - `reportée` : intéressante, mais pas maintenant ; la raison est donnée ;
    - `refusée` : hors périmètre, trop coûteuse à maintenir, ou incompatible ; la raison est donnée.
5. **Réaliser** : le porteur ouvre une demande de fusion, qui suit la liste de contrôle ci-dessous.
6. **Publier** : la fonctionnalité sort avec la version suivante du module.

Une correction simple (faute, lien, bogue évident) n'a pas besoin d'issue préalable : une demande de fusion directe suffit.

## Critères d'intégration

Une proposition est retenue si elle :

- **reste dans le périmètre** du module (un module fait une chose, bien) ;
- **est désactivée par défaut** quand elle change un comportement existant, ou compatible avec les configurations déjà enregistrées ;
- **a été essayée dans un vrai GEO**, avec la version de GEO précisée ; ce qui n'a pas été validé est signalé dans la description ;
- **met à jour** le journal des nouveautés (`CHANGELOG.md`, pour les utilisateurs), la version et, si besoin, le README ;
- **respecte les conventions** du module (messages de commit, langue, nommage) décrites dans son `CONTRIBUTING.md` ;
- **peut être maintenue** par une autre personne que son auteur : code lisible, pas de dépendance fragile ou propriétaire ;
- **ne contient ni secret, ni donnée personnelle**, et respecte les licences des dépendances (compatibles GPL-3.0).

Une fonctionnalité qui ajoute une dépendance, un service externe ou un appel réseau est examinée plus attentivement : elle doit préciser ce qui
est envoyé, à qui, et ce qui se passe si le service est indisponible.

## Fusion, reprise et publication

Les dépôts GitHub des modules sont alimentés depuis le **dépôt source de la collectivité**. Cela a une conséquence pratique, que nous préférons
écrire plutôt que laisser deviner :

- les mainteneurs **fusionnent** la demande de fusion sur GitHub après relecture ;
- le contenu est **repris dans le dépôt source**, avec les auteurs d'origine conservés ;
- il est **publié avec la version suivante** du module, dans un commit de synthèse qui mentionne les contributeurs (`Co-authored-by`).

Les commits d'origine restent visibles sur GitHub, mais n'ont pas le même identifiant dans le dépôt source : seul le contenu fait référence.
Les contributions sont citées dans le `README.md` du module concerné.

**Délais visés** *(à valider)* : première réponse à une issue ou une demande de fusion sous une semaine ; publication de la version suivante dans
le mois qui suit la fusion.

### Versions

Les modules suivent le versionnement sémantique : une correction incrémente le dernier chiffre, une fonctionnalité le deuxième, un changement
incompatible (réglage renommé ou supprimé, par exemple) le premier. Le numéro de version est fixé par les mainteneurs au moment de la publication
et reporté à l'identique dans `package.json`, `src/plugin.geoext.json` et `CHANGELOG.md`.

## Suivi des travaux

Une **feuille de route publique** est prévue sous la forme d'un tableau de projet GitHub d'organisation, alimenté par les issues des dépôts de
modules *(à mettre en place)*. Statuts envisagés : *Idée*, *À faire*, *En cours*, *À rapatrier*, *À publier*, *Publié*. Il permet à chacun de voir
ce qui est prévu, ce qui avance et ce qui attend une relecture.

## Où discuter de quoi

| Besoin | Où |
|---|---|
| Une question, une astuce, un retour d'expérience | [Discord du Club Utilisateurs GEO](contribuer.md#echanger-avec-la-communaute) |
| Un bogue, une idée, une proposition | Issue du dépôt du module concerné |
| Une modification de code ou de documentation | Demande de fusion sur le dépôt du module |
| Le site, la gouvernance, un sujet transversal | Issue de [geo-modules-community](https://github.com/vienne-condrieu-agglomeration/geo-modules-community/issues) |

## Licences et origine des contributions

En contribuant, vous acceptez que votre contribution soit publiée sous les licences du projet. Chaque commit porte une ligne `Signed-off-by`
([Developer Certificate of Origin](https://developercertificate.org/)) : elle atteste que vous avez le droit de proposer ce que vous envoyez.
Voir [Contribuer](contribuer.md).

## Questions ouvertes

Points à trancher ensemble :

- Les **délais** de réponse et de publication ci-dessus sont-ils tenables et utiles ?
- Quel **mode d'invitation** des co-mainteneurs, et sur quels modules ?
- Les **droits d'écriture** : demandes de fusion relues pour tout le monde, ou accès direct pour des co-mainteneurs de confiance ?
- Peut-on **proposer un module nouveau** dans la bibliothèque, et selon quels critères (périmètre, maintenance, licence) ?
- Faut-il un **code de conduite** pour le Discord et les dépôts ?
