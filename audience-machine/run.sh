#!/usr/bin/env bash
# Run the machine for ONE client, using the .venv sandbox automatically.
#
#   ./run.sh config/clients/acme.yml --dry-run     # preview
#   ./run.sh config/clients/acme.yml               # build for real
#
set -e
cd "$(dirname "$0")"

if [ ! -x ".venv/bin/python" ]; then
  echo "Sandbox not found. Run ./setup.sh first." >&2
  exit 1
fi
exec ./.venv/bin/python create_audiences.py "$@"
