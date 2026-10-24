## Ce que change cette demande

<!-- Le quoi et le pourquoi, en quelques lignes. Lier l'issue concernée si elle existe. -->

## Liste de contrôle

- [ ] `zensical build --clean` passe sans avertissement (la construction en PR le vérifie aussi).
- [ ] `python scripts/check_links.py` ne signale aucune erreur.
- [ ] Une nouvelle page écrite à la main est ajoutée au `nav` de `zensical.toml`.
- [ ] Les pages `developper/` ne contiennent ni identifiant, ni chemin de service interne, ni module non publié ; ce qui n'est pas validé sur un GEO est marqué ❓.
- [ ] Les commits suivent les [Conventional Commits](https://www.conventionalcommits.org/fr/v1.0.0/) et portent un `Signed-off-by` (`git commit -s`).
