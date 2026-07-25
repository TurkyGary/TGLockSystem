#!/usr/bin/env bash
set -euo pipefail
# -e: stop when a command fails.
# -u: stop when undefined variable is used.
# pipefail: detect failure anywhere in a pipeline.

## Fetch remote repo and discard local changes ##

# 1. Fetch the latest metadata and commits from Github without merging
git fetch origin

# 2. Hard reset current local branch to math the remote branch.
git reset --hard origin/main

# Clean all untracked files and directories (-f = force, -d = directories)
git clean -fd
