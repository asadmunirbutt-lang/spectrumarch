#!/usr/bin/env bash
# Deploy this folder straight to Azure Static Web Apps from your own computer.
# No GitHub connection is required.
#
# One-time setup:
#   npm install -g @azure/static-web-apps-cli
#
# Usage (the token is read from the environment, never saved to disk):
#   export SWA_CLI_DEPLOYMENT_TOKEN='<paste token from Azure portal>'
#   ./deploy.sh
set -euo pipefail
cd "$(dirname "$0")"

if [ -z "${SWA_CLI_DEPLOYMENT_TOKEN:-}" ]; then
  echo "Set SWA_CLI_DEPLOYMENT_TOKEN first (Azure portal > your Static Web App > Overview > Manage deployment token)." >&2
  exit 1
fi

# Stage only the public site files so notes and scripts are never uploaded.
STAGE="$(mktemp -d)"
trap 'rm -rf "$STAGE"' EXIT
cp -R *.html favicon.svg robots.txt sitemap.xml staticwebapp.config.json assets blog "$STAGE"/

swa deploy "$STAGE" --env production
