#!/usr/bin/env bash
set -euo pipefail

RG="rg-devsecops-lab"
LOC="westeurope"
ACR="acrhemanthdevsecops01"

echo "Creating Resource Group: $RG in $LOC"
az group create --name "$RG" --location "$LOC" -o table

echo "Creating ACR: $ACR"
az acr create --resource-group "$RG" --name "$ACR" --sku Basic -o table

echo "Done."
echo "RG=$RG"
echo "ACR=$ACR"
