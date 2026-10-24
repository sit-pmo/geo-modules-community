# Le manifeste `plugin.geoext.json` et le Générateur

- ⚠️ **`ENUMERATED` : le Générateur affiche les `values` et ignore `labels`** (testé en 4.5.0). Mettez le texte lisible dans `values` et convertissez-le
  dans le code.
- ⚠️ **Les noms d'attributs sont tronqués à 28 caractères** dans les résultats de recherche GEO.
- ⚠️ **Dépendance à l'API GEO facultative** : déclarer `bg.common.geo.GeoApi` en dépendance Angular fixe empêche **toute l'application** de démarrer
  (`[$injector:nomod] Module 'bg.common.geo.GeoApi' is not available`) si le module « GEO API JS v2 » n'est pas ajouté à l'application. Pour un module qui
  doit fonctionner sans lui, ne déclarez que `bg.acf.base`, ajoutez le module GeoApi à l'exécution s'il existe et obtenez `geoApplication` par
  `$injector`. (Le cas « API absente » n'a pas été testé.)
- ⚠️ **GEO refuse de réimporter un ZIP déjà importé sous le même nom** : datez le nom du ZIP (`mon-module_AAAAMMJJ-HHMM.zip`).
- ⚠️ La `version` qui fait foi pour GEO est celle de `plugin.geoext.json`. Gardez-la identique à celle de `package.json`.
- ⚠️ L'import d'un module se fait dans l'**ancienne interface** du Générateur (Modules > + Module), pas dans la nouvelle.
- ⚠️ `npm run publish` (envoi direct au serveur) peut répondre par une **erreur 500** avec un gros bundle (~2,9 Mo constaté ; cause non confirmée).
  Importez le ZIP à la main.
- Une valeur de configuration doit tolérer l'absence : `props.x !== false` pour un booléen vrai par défaut. Un réglage supprimé laisse des valeurs
  enregistrées qui sont simplement ignorées.
