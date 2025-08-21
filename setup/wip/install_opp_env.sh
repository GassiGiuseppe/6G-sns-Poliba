#!/usr/bin/env bash
set -euo pipefail

# Prevent running as root
if [ "$(id -u)" -eq 0 ]; then
  echo "Error: do not run this script as root (no sudo)."
  exit 1
fi

# Define conda environment and path
#ENV_NAME="py310"
ENV_NAME="base" # the correct one to use is py310 but there are currently some issues
MINICONDA_PATH="$HOME/miniconda"

# Ensure conda is available
if [ ! -x "$MINICONDA_PATH/bin/conda" ]; then
  echo "Error: Conda not found at $MINICONDA_PATH"
  exit 1
fi

# 1. Install Nix if not present
if ! command -v nix &> /dev/null; then
  echo "Nix not found. Installing..."
  curl -L https://nixos.org/nix/install | sh

  if [ -f "$HOME/.nix-profile/etc/profile.d/nix.sh" ]; then
    . "$HOME/.nix-profile/etc/profile.d/nix.sh"
  else
    echo "Error: Nix installed but profile script not found."
    exit 1
  fi
else
  echo "Nix already installed."
  . "$HOME/.nix-profile/etc/profile.d/nix.sh"
fi

# 2. Initialize Conda in this shell, THIS HERE ITS THE CRRECT WAY BECAUSE CONDA IS JUST INSTALLED, NO REBOOT HAS HAPPENED
echo "Initializing Conda from: $MINICONDA_PATH"
eval "$("$MINICONDA_PATH/bin/conda" shell.bash hook)"

# 3. Activate the Conda environment
echo "Activating Conda environment: $ENV_NAME"
conda activate "$ENV_NAME"

# 4. Install opp_env
echo "Installing opp_env package..."
pip install --upgrade opp_env

# 5. Run OMNeT++ environment setup
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
bash "$SCRIPT_DIR/setup_sim_env.sh"

echo "Setup completed in environment '$ENV_NAME' with OMNeT++ tools configured."
