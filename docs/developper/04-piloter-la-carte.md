# Piloter la carte GEO sans la dérégler

✅ **Pour recentrer sans changer le zoom, utilisez `map.centerOn({ coordinates, crs })`.** Mesures faites sur GEO :

- `setExtent(emprise courante, crs, { disablePadding: true })` **ne restitue pas le zoom** : largeur ×1,333 panneau fermé, ×1,5 panneau ouvert.
  Appelé à chaque changement de photo, il dézoomait de façon cumulative ;
- `panTo(direction)` décale d'un cran (nord, est…) et **ignore sans rien dire** des coordonnées ;
- `centerOn` déplace le centre exactement. Pour qu'un repère tombe au milieu de la zone **visible** quand un panneau masque une partie de la carte,
  décalez le centre visé vers l'est de `(0,5 − f) × largeur`, avec `f = (100 − largeurPanneauEnPourcent) / 200`.

- ✅ Clic sur la carte : `geoApplication.map.on('pointerClick', callback)`. Convertissez les coordonnées en EPSG:4326 avec `geoApplication.transform`
  si le système de la carte est différent. **Gardez le retour de `on()` et de `watch()`** et appelez `.unsubscribe()` à la fermeture.
- ✅ Un événement peut arriver **deux fois** pour le même objet : dédoublonnez sur son identifiant.
- ✅ Si l'utilisateur doit tracer sur la carte GEO pendant qu'un panneau couvre une vue 3D, grisez la vue, bloquez son pointage et affichez
  « Cliquez sur la carte », avec un bouton annuler. Sans cela, il ne comprend pas où tracer.
