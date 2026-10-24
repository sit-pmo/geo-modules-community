# Développer un module GEO

Ce document rassemble ce que nous avons **constaté en pratique** en développant des modules pour la plateforme GEO de Business Geografic
(par exemple [geo-module-panoramax](https://github.com/vienne-condrieu-agglomeration/geo-module-panoramax) et
[geo-module-compare-swipe](https://github.com/vienne-condrieu-agglomeration/geo-module-compare-swipe)). Il s'adresse aux personnes qui veulent
corriger un de ces modules ou en écrire un nouveau.

!!! warning "À lire d'abord"
    - Ce n'est **pas** la documentation officielle. Celle-ci décrit l'API JavaScript GEO utilisée dans une page autonome ; un module déployé tourne
    dans un contexte différent, et c'est là que viennent la plupart des écarts. Documentation officielle :
    <https://docgeoapi.business-geografic.com/fr/guide/4-Modules/introduction>.
    - Plusieurs services mentionnés ici (`acfExtensionService`, `acfMapService`…) sont des **services internes de la plateforme, non documentés** :
    ils peuvent changer sans préavis d'une version de GEO à l'autre. Les modules publiés les utilisent, la liste n'est pas une garantie de stabilité.
    - Les constats viennent de tests sur des versions précises du Générateur (4.5.0 pour la plupart). **Validez toujours sur votre serveur GEO.**

Légende : ✅ constaté et validé sur GEO · ⚠️ piège rencontré · ❓ hypothèse ou non testé.

## Sommaire

1. [Le contexte d'exécution d'un module déployé](01-contexte-execution.md)
2. [Enregistrer l'interface](02-interface.md)
3. [Cartes secondaires et synchronisation](03-cartes-secondaires.md)
4. [Piloter la carte GEO sans la dérégler](04-piloter-la-carte.md)
5. [Le manifeste `plugin.geoext.json` et le Générateur](05-manifeste-generateur.md)
6. [Angular, éléments personnalisés, timing](06-angular-timing.md)
7. [Build et dépendances](07-build.md)
8. [Interface et CSS](08-css.md)
9. [Données externes](09-donnees-externes.md)
10. [Méthode de débogage qui a marché](10-debug.md)
11. [Ce qui a bien marché](11-reussites.md)
