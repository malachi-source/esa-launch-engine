#!/usr/bin/env bash
# Build audiences for ALL clients at once. Loops over every config in
# config/clients/ (except the example template). This is the "all clients
# simultaneously" button: fill a config per client, then run this.
#
#   ./run_all.sh --dry-run     # preview every client
#   ./run_all.sh               # build every client for real
#
set -e
cd "$(dirname "$0")"

if [ ! -x ".venv/bin/python" ]; then
  echo "Sandbox not found. Run ./setup.sh first." >&2
  exit 1
fi

shopt -s nullglob
clients=(config/clients/*.yml)
ran=0
for cfg in "${clients[@]}"; do
  case "$cfg" in
    *example-client.yml) continue ;;   # skip the template
  esac
  echo ""
  echo "############################################################"
  echo "# CLIENT: $cfg"
  echo "############################################################"
  ./.venv/bin/python create_audiences.py "$cfg" "$@" || echo "(client $cfg had errors; continuing)"
  ran=$((ran+1))
done

if [ "$ran" -eq 0 ]; then
  echo "No client configs found. Copy config/clients/example-client.yml to add one."
fi
echo ""
echo "All done. Summaries are in output/."
