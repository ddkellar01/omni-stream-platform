#!/usr/bin/env bash
set -e

echo "[*] Initializing OmniStream Platform Monorepo..."

# Create core directory tree
mkdir -p services/{api-gateway,auth-manager,video-ingest-service,transcoding-worker,streaming-service,metadata-service,promotion-orchestrator,media-transformer,analytics-aggregator}
mkdir -p services/integrations/{facebook-adapter,x-adapter,instagram-adapter,snapchat-adapter,youtube-adapter}
mkdir -p infra/{terraform,kubernetes}
mkdir -p clients/{web-player,publisher-dashboard}
mkdir -p docs .github/workflows

echo "[+] Directory structure created successfully."
