#!/usr/bin/env bash
# Run the foundation machine, using the .venv sandbox automatically.
#
#   ./run.sh --sample                 # build the master brain from the bundled sample
#   ./run.sh --sample --ad-scripts    # ...and generate the ad scripts too
#   ./run.sh --latest                 # read the newest real submission from Supabase
#   ./run.sh --sample --dry-run       # show the plan, call nothing
#
set -e
cd "$(dirname "$0")"

if [ ! -x ".venv/bin/python" ]; then
  echo "Sandbox not found. Run ./setup.sh first." >&2
  exit 1
fi
exec ./.venv/bin/python foundation.py "$@"
