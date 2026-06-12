#!/usr/bin/env bash
# ONE-TIME setup. Run this once after cloning. It builds a private little
# Python sandbox (.venv) and installs the 2 packages the tool needs.
#
#   cd audience-machine
#   ./setup.sh
#
set -e
cd "$(dirname "$0")"

echo "Creating Python sandbox (.venv) ..."
python3 -m venv .venv

echo "Installing packages (requests, pyyaml) ..."
./.venv/bin/pip install --quiet --disable-pip-version-check -r requirements.txt

echo ""
echo "Done. The machine is ready."
echo "Next: open TOKEN_SETUP.md to create your Meta token, then:"
echo "  export META_ACCESS_TOKEN=\"your-token\""
echo "  ./run.sh config/clients/example-client.yml --dry-run"
