# Enregistrer l'interface

✅ Deux enregistrements utilisés par les modules publiés, via `acfExtensionService` :

```js
// Onglet de la barre latérale droite
acfExtensionService.registerWidgetExtension({
    type: window.bgCanvasId === 'pro1' ? 'rightPanel' : 'widget.side',
    key: pluginConf.name, extensionKey: pluginConf.name,
    name: toolName, icon: 'icon icon_compare', active: false, widthPolicy: 'custom',
    enable: function () { return true; },
    template: buildTemplate(), controller: buildController(),
    configure: function (ext) { widgetId = ext && ext.id ? ext.id : pluginConf.name; }
});

// Bouton de la barre d'outils de la carte
var ext = acfExtensionService.registerMapToolExtension({
    key: pluginConf.name, name: toolName, icon: 'icon icon_compare',
    content: '<span class="icon icon_compare" aria-hidden="true"></span>',
    position: 'topleft', priority: 100, disableMobileapp: true,
    handle: function () { toggle(); }
});
```

- ⚠️ Le bouton de carte n'accepte que le couple **`icon` + `handle`** (et `content` pour l'icône) : un `template` ou un `controller` y est ignoré.
- ✅ **Élargir le panneau** : `$rootScope.$broadcast('EXTENSION_WIDGET_ACTION', { action: 'setPanelSize', widgetId: widgetId, width: 50 })` (largeur en %).
  ⚠️ Sans le **bon `widgetId`** (celui reçu dans `configure`), le message cible un autre widget. Après un changement de taille, déclencher
  `window.dispatchEvent(new Event('resize'))` : les bibliothèques de rendu se redimensionnent sur cet événement.
- ✅ Savoir quand l'onglet s'ouvre : `$rootScope.$on('activeRightTabChanged', function (e, tabId) { … })`.
- ⚠️ Nous n'avons trouvé **aucune API pour fermer le panneau**. Une confirmation « voulez-vous ouvrir ? » doit donc vivre **dans** le panneau.
- ✅ **Zones du gabarit** : le Générateur compare `compatibleZoneTags` aux étiquettes des zones d'extension du gabarit. Étiquettes relevées avec le
  Générateur 4.5.0 : en-tête `widget.header(.pro)`, impression `widget.print(.pro)`, carte `map(.pro)`, bandeau de droite `widget.side(.pro)`.
  Avec le seul tag `global.pro`, le module n'apparaît que dans la liste globale des modules de l'application.
