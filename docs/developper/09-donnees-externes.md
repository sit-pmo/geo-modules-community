# Données externes

- ✅ **WFS de l'IGN** : `BBOX` en `lon,lat,lon,lat,EPSG:4326`. Le service limite le débit (**HTTP 429**) : trois requêtes simultanées au plus, avec reprise.
- ✅ **Rasters d'altitude** : WMS `FORMAT=image/x-bil;bits=32` renvoie des flottants bruts, sans dépendance GeoTIFF.
- ✅ **Précision 3D** : les coordonnées monde en float32 dans un shader donnent environ 0,25 m ; dessinez en coordonnées **locales** avec
  `mesh.position` pour éviter le tremblement.
- ✅ **Export DXF** : relu sans problème par GDAL et QGIS ; non testé dans AutoCAD ni Covadis.
