#!/usr/bin/env bash
# ONE-TIME setup. Run this once. Builds a private Python sandbox (.venv) and
# installs the one package the machine needs (requests).
#
#   cd foundation-machine
#   ./setup.sh
#
set -e
cd "$(dirname "$0")"

echo "Creating Python sandbox (.venv) ..."
python3 -m venv .venv

echo "Installing packages (requests) ..."
./.venv/bin/pip install --quiet --disable-pip-version-check -r requirements.txt

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Created .env from the template."
fi

echo ""
echo "Done. The machine is ready."
echo "Next:"
echo "  1) Open .env and paste your ANTHROPIC_API_KEY  (open -e .env)"
echo "  2) Test it:   ./run.sh --sample --ad-scripts"
