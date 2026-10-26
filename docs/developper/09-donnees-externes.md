# Données externes

- ✅ **WFS de l'IGN** : `BBOX` en `lon,lat,lon,lat,EPSG:4326`. Le service limite le débit (**HTTP 429**) : trois requêtes simultanées au plus, avec reprise.
- ✅ **Rasters d'altitude** : WMS `FORMAT=image/x-bil;bits=32` renvoie des flottants bruts, sans dépendance GeoTIFF.
- ✅ **Précision 3D** : les coordonnées monde en float32 dans un shader donnent environ 0,25 m ; dessinez en coordonnées **locales** avec
  `mesh.position` pour éviter le tremblement.
- ✅ **Export DXF** : relu sans problème par GDAL et QGIS ; non testé dans AutoCAD ni Covadis.
- ✅ **Fichiers statiques sur GitHub Pages** : les réponses portent `access-control-allow-origin: *`, donc GEO peut les lire. Utilisez le `fetch` du
  navigateur avec `credentials: 'omit'`, **pas `$http`** : les intercepteurs de GEO pourraient joindre des en-têtes d'authentification à une adresse
  tierce, ce qui échoue en CORS et divulguerait un jeton. Un module qui lit des données externes doit annoncer sa source et sa date.
- ✅ **API Carto Cadastre de l'IGN** (`apicarto.ign.fr/api/cadastre/parcelle`) : renvoie le contour d'une parcelle (MultiPolygon en EPSG:4326, avec
  `idu`, `contenance`, `nom_com`) avec CORS ouvert. Passez `code_insee`, `section` sur 2 caractères (`0A` pour « A »), `numero` sur 4 chiffres et
  `com_abs` (préfixe de section, `000` par défaut). Une parcelle qui n'existe plus renvoie 0 entité, pas une erreur.
- ❓ **Recherche de GEO appelée par programme** : après un premier `Services.Search.executeSearch`, les appels suivants n'aboutissent plus (« too much
  recursion » dans le `$emit` de GEO, constaté sur GEO 4.5.0). La cause n'est pas établie. Les filtres sont des références (`targetId`) à résoudre par
  `geoApplication.getResourceById`, et l'arbre de filtres s'appelle `filtersTree`. Pour un besoin simple, une API externe est plus fiable.
- ✅ **Listes liées dans un module** (commune, section, numéro) : construisez-les avec vos propres données plutôt qu'avec les filtres liés d'une
  recherche GEO. Pour des milliers d'options, `datalist` remplie en JavaScript est bien plus rapide qu'un `ng-repeat` ; pour quelques dizaines de choix
  fixes, préférez une liste déroulante, qui interdit les saisies hors périmètre.
