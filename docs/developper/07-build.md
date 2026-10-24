# Build et dépendances

- ⚠️ Les modules utilisent **webpack 4**. Une bibliothèque récente peut dépasser son analyseur (`Module parse failed: Unexpected token` sur `??=`,
  `?.`, champs de classe, blocs statiques).
  ⚠️ **N'utilisez pas `@babel/preset-env`** sur un gros fichier : la compilation réussit mais l'exécution casse (`TypeError: n is not a function`).
  ✅ Utilisez des **plugins Babel ciblés** (`@babel/plugin-transform-optional-chaining`, `-nullish-coalescing-operator`, `-logical-assignment-operators`,
  `-class-static-block`, `-class-properties`, `-private-methods`, `-private-property-in-object`), en ajoutant celui qui correspond à la nouvelle erreur.
- `angular` va toujours dans `externals` : la plateforme le fournit.
- ✅ **Figez les versions** des bibliothèques lourdes : un module est livré en ZIP, sans mise à jour automatique.
- ✅ Un gros calcul peut tourner dans un *worker* instancié depuis un **Blob** (`URL.createObjectURL(new Blob([source]))`).
- Ne commitez ni `dist/`, ni `node_modules`, ni le ZIP.
