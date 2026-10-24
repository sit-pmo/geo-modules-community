---
icon: lucide/download
---

# Installer un module

Un module GEO est un **ZIP** qui contient sa fiche (`plugin.geoext.json`) et son code (`main.js`). Chaque version publiée est jointe à la page
**Releases** du dépôt du module (bouton « Télécharger le ZIP » sur la page de chaque [module](modules/index.md)).

## Prérequis

- Un Générateur GEO et une application GEO. Chaque module indique la **version minimale de GEO** qu'il suppose.
- Le module « GEO API JS v2 » ajouté à l'application : les modules s'en servent pour lire leurs réglages. Sans lui, certains modules ne
  fonctionnent pas.

## Étapes

1. **Téléchargez le ZIP** de la dernière version depuis la page du module.
2. Dans le Générateur, ouvrez **Modules**, puis **+ Module**, et importez le ZIP.

    !!! warning "Ancienne interface"
        L'import de modules se fait dans l'**ancienne interface** du Générateur, pas dans la nouvelle.

3. **Glissez le module** dans l'application, à l'emplacement prévu (la liste des modules de l'application, ou une zone du gabarit si le module
   le permet).
4. **Renseignez les réglages** du module : le Générateur construit l'écran de configuration à partir de la fiche du module.
5. **Enregistrez**, puis ouvrez l'application et essayez le module.

## Mise à jour

Importez le ZIP de la nouvelle version de la même façon. Le Générateur peut refuser un ZIP **déjà importé sous le même nom** : si le fichier
porte le même nom que le précédent, renommez-le (par exemple en y ajoutant la date).

## En cas de problème

- Ouvrez la console du navigateur (touche **F12**) : les modules y signalent leurs erreurs avec un préfixe `[nom-du-module]`.
- Vérifiez la version de GEO et les réglages du module.
- Si le problème persiste, [signalez-le](contribuer.md) sur le dépôt du module, en indiquant la version du module, la version de GEO et le
  message de la console.
