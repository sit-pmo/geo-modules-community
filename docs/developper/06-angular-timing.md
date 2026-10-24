# Angular, éléments personnalisés, timing

- ⚠️ **Notation tableau obligatoire** pour toute injection (`['geoApplication', function (geoApplication) { … }]`) : la minification renomme les
  paramètres (`Unknown provider: eProvider <- e`). Valable pour `.run`, `.controller`, `.service`, `.factory`, `.directive`.
- ⚠️ Un **élément personnalisé** (custom element) lit ses attributs dès sa connexion au DOM, avant le cycle Angular : posez ses attributs **en
  JavaScript**, jamais par `{{interpolation}}`.
- ⚠️ **Ne posez pas en statique un attribut qui est déjà la valeur par défaut** : dans notre cas, `focus="pic"` sur le composant `<pnx-viewer>`
  provoquait `Uncaught Error: Map is not enabled`. L'explication est une hypothèse (le composant réagit avant que sa carte interne soit prête),
  la correction a été validée.
- ⚠️ Un `input[type=range]` compilé d'emblée affiche une mauvaise valeur : placez-le derrière un `ng-if`.
- ⚠️ **GEO échoue souvent en silence.** Mettez un `console.error('[nom-module] …')` dans chaque branche de repli, et ouvrez la console (F12).
- ✅ `localStorage` convient aux préférences (« ne plus demander », visite faite), toujours dans un `try/catch` : il peut être bloqué (navigation privée).
- ✅ Appuyez-vous sur l'**API publique documentée** d'une bibliothèque tierce (attributs, méthodes, événements) plutôt que sur ses appels internes, et
  vérifiez la version réellement installée (`npm ls`).
