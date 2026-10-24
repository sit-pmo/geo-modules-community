# Le contexte d'exécution d'un module déployé

⚠️ **`window.geo` n'est pas l'API GEO** dans une extension déployée : l'objet existe mais ne contient pas `Application`. Les appels
`new geo.Application(…)`, `geo.application(…)` ou `geo.createApplication(…)` échouent **sans erreur** : panneaux vides, console muette. Les modules
publiés ne créent donc aucune sous-application GEO.

✅ Ce qui marche à la place :

| Besoin | Accès |
|---|---|
| Façade applicative | `geoApplication` (injecté dans `.run`). ❓ Sa surface semble plus limitée que dans la documentation de l'API autonome : à vérifier sur votre version avant de s'appuyer sur `getBaseLayerById` ou `getBaseLayersByName` |
| Carte OpenLayers principale | `$injector.get('acfMapService').getMapViewImmediate().getNativeMap()` |
| Étendue, centre, zoom | `mapView.getExtent()`, `getCenter()`, `getZoom()`, `getResolution()`, `getCrs()` |
| OpenLayers complet | `window.ol` |
| Fonds de plan applicatifs | `geoApplication._baseLayers` (objet `id → descripteur`) |

Entourez l'accès à la carte d'un `try/catch` avec un `console.warn` : la carte peut ne pas être disponible au moment de l'appel.

⚠️ Une copie locale de la plateforme ou de sa documentation peut différer de la version déployée chez vous. Ce qu'on y lit n'est pas fiable : validez
en direct dans l'application.
