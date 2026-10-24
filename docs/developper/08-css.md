# Interface et CSS

- ✅ **Icônes natives** : combinez toujours `class="icon icon_xxx"`. Seule la classe `.icon` apporte la police d'icônes ; sans elle s'affiche le
  codepoint brut (« F131 »).
- ⚠️ **Icône personnalisée dans l'onglet** : l'élément qui la porte est aussi un `.launcher-icon` de GEO dont la taille vient du thème. Portez le masque
  CSS par `::before` en `1em`, qui suit le `font-size` de chaque contexte.
- ⚠️ **Empilement** : une fenêtre à `z-index` élevé qui ferme sur Échap capte les touches d'une modale créée en dessous. Une modale doit accepter un
  `z-index` configurable et gérer Échap et Tab.
- ⚠️ **Évitez les positions en pixels fixes.** La barre d'outils se replie sur deux lignes quand le panneau est étroit : mesurez la hauteur réelle
  (`ResizeObserver`) et publiez-la en variable CSS. ⚠️ Le panneau **glisse en place et reçoit sa largeur après coup** : une mesure unique à l'ouverture
  voit zéro. Remesurez à intervalles après l'ouverture et à chaque redimensionnement de la carte.
- ⚠️ Deux panneaux au même emplacement se masquent : regroupez-les.
- ✅ **Préfixez toutes vos classes CSS** (`geo-<module>-…`) : les styles de GEO sont globaux.
- ✅ Variables de thème réutilisables : `--primaryColor`, `--accentColor`.
- ✅ Un réglage ajouté en bas d'un long panneau passe inaperçu : placez-le dans une section visible.
