# Cartes secondaires et synchronisation

✅ Pour afficher plusieurs cartes (comparaison, loupe…) : une **`ol.Map` native par panneau et une seule `ol.View` partagée**. Le déplacement et le
zoom se propagent sans verrou anti-boucle. Si la synchronisation est désactivable, donnez à chaque carte une copie de la vue.

- ⚠️ `ol.control.defaults` n'est pas appelable selon le build d'OpenLayers de la plateforme : utilisez `controls: []`.
- ⚠️ **Carte créée à 0×0** : si le `<div>` est masqué ou sans taille au moment du `new ol.Map`, aucune tuile ne charge. Attendez une taille non
  nulle (un court `setTimeout` répété) et appelez `map.updateSize()` quand le panneau redevient visible.
- ⚠️ **`geoApplication._baseLayers` est vide au démarrage** : il n'est rempli qu'après l'initialisation complète de l'application. Lisez-le à
  l'ouverture de votre interface (action de l'utilisateur), pas dans `executeWhenInitialized`, et construisez vos couches **à ce moment-là**.
- ✅ **Deux modes de fonds de plan** (Générateur, « Gérer les fonds de plan dans la carte ») : désactivé, les fonds sont composés côté serveur en une
  seule tuile GEO ; activé, ce sont de vraies couches OpenLayers. Construire vos couches depuis `_baseLayers` fonctionne dans les deux cas.
- Construction par type de connexion : WMTS → lire les *GetCapabilities* puis `ol.source.WMTS.optionsFromCapabilities` (essayer l'identifiant puis le
  nom de la couche) ; WMS → `ol.source.TileWMS` ; XYZ/TMS → `ol.source.XYZ`.
- ⚠️ **Fonds protégés** : ne contournez pas l'authentification de la plateforme. Un fond servi derrière le proxy de GEO doit rester servi par ce
  proxy ; n'allez pas chercher d'identifiants dans la configuration côté navigateur.
- ⚠️ La lecture des *GetCapabilities* par `fetch` est soumise au **CORS** (le chargement des tuiles en `<img>` ne l'est pas). Si le serveur ne
  renvoie pas les en-têtes CORS, construisez la grille de tuiles WMTS à la main.
