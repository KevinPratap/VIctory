#!/usr/bin/env bash
# Commits files to the forge/status branch and pushes it (docs/forge.md).
# Usage: .github/forge-publish.sh "<commit message>" <file>...
# Run from the repository's checkout in a GitHub Actions job whose token may
# write contents. The branch is created (orphan) on first use. The Forge and
# the claims workflows both publish here, so a rejected push is retried on top
# of the other's commit.
set -euo pipefail
message=$1
shift
dir=$(mktemp -d)
root=$(pwd)
trap 'git -C "$root" worktree remove --force "$dir" 2>/dev/null || true' EXIT
if git fetch -q origin forge/status 2>/dev/null; then
  git worktree add -q "$dir" FETCH_HEAD
else
  git worktree add -q --detach "$dir"
  git -C "$dir" checkout -q --orphan forge-status-new
  git -C "$dir" rm -rqf . 2>/dev/null || true
fi
cp "$@" "$dir"/
cd "$dir"
git add -- "${@##*/}"
if git diff --cached --quiet; then
  echo "nothing changed"
  exit 0
fi
git commit -q -m "$message"
for attempt in 1 2 3; do
  if git push -q origin HEAD:refs/heads/forge/status; then
    exit 0
  fi
  git fetch -q origin forge/status
  git rebase -q FETCH_HEAD
done
echo "could not push forge/status" >&2
exit 1
