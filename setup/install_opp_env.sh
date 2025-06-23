#!/usr/bin/env bash
set -euo pipefail

# Protezione: blocca esecuzione come root
if [ "$(id -u)" -eq 0 ]; then
  echo "Errore: non eseguire questo script come root (niente sudo)."
  exit 1
fi

# Definizione ambiente Conda
ENV_NAME="py310"
USER_HOME=$(eval echo ~${SUDO_USER:-$USER})
MINICONDA_PATH="$USER_HOME/miniconda"

# 1. Installa Nix se non presente
if ! command -v nix &> /dev/null; then
  echo "Nix non trovato. Installazione in corso..."
  curl -L https://nixos.org/nix/install | sh

  # Attiva Nix per questa shell
  if [ -f "$HOME/.nix-profile/etc/profile.d/nix.sh" ]; then
    . "$HOME/.nix-profile/etc/profile.d/nix.sh"
  else
    echo "Errore: installazione Nix completata ma non trovata nel profilo."
    exit 1
  fi
else
  echo "Nix è già installato."
  . "$HOME/.nix-profile/etc/profile.d/nix.sh"
fi

# 2. Inizializza Conda
echo "Inizializzo Conda dal path: $MINICONDA_PATH"
eval "$($MINICONDA_PATH/bin/conda shell.bash hook)"

# 3. Attiva l’ambiente Conda esistente
echo "Attivo ambiente conda '$ENV_NAME'"
conda activate "$ENV_NAME"

# 4. Installa opp_env
echo "Installo opp_env"
pip install --upgrade opp_env

# 5. Esegui lo script di setup ambiente OMNeT++
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$SCRIPT_DIR/setup_sim_env.sh"

echo "Tutto installato in $ENV_NAME + simu5g-env"
