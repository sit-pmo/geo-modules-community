#!/usr/bin/env bash
# Crée ou met à jour les labels de scripts/labels.json sur les dépôts GitHub indiqués (action sur GitHub : nécessite « gh auth login »).
# Usage : scripts/sync_labels.sh organisation/depot [organisation/depot ...]
# Un label déjà présent est mis à jour (--force) ; aucun label n'est supprimé.
set -euo pipefail
cd "$(dirname "$0")/.."
[ $# -gt 0 ] || { echo "Usage : $0 organisation/depot [organisation/depot ...]" >&2; exit 1; }
command -v gh >/dev/null || { echo "gh (GitHub CLI) est requis" >&2; exit 1; }
command -v jq >/dev/null || { echo "jq est requis" >&2; exit 1; }
for repo in "$@"; do
    echo "== $repo"
    jq -c '.[]' scripts/labels.json | while read -r label; do
        name=$(jq -r .name <<<"$label")
        gh label create "$name" --repo "$repo" --color "$(jq -r .color <<<"$label")" \
            --description "$(jq -r .description <<<"$label")" --force >/dev/null
        echo "   $name"
    done
done
