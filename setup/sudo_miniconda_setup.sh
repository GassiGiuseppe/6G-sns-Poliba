#!/bin/bash
set -euo pipefail

# Script name: sudo_miniconda_setup.sh
# Description: Installs Miniconda into the regular user's home directory
#              and sets up a Python 3.10 environment, usable by that user.

# Miniconda source
MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
INSTALLER="Miniconda3-latest-Linux-x86_64.sh"

# Detect the non-root user who invoked the parent sudo script
USER_NAME="${SUDO_USER:?Error: SUDO_USER not set}"
USER_HOME="$(eval echo "~$USER_NAME")"

# 1. Install dependencies
apt update && apt install -y curl bzip2

# 2. Download the Miniconda installer
curl -o "$INSTALLER" "$MINICONDA_URL"

# 3. Install Miniconda to the user's home directory
bash "$INSTALLER" -b -p "$USER_HOME/miniconda"

# 4. Set correct ownership
chown -R "$USER_NAME:$USER_NAME" "$USER_HOME/miniconda"

# 5. Initialize Conda for the user (adds to their .bashrc)
sudo -u "$USER_NAME" "$USER_HOME/miniconda/bin/conda" init bash

# 6. Create a Python 3.10 environment as the user
sudo -u "$USER_NAME" "$USER_HOME/miniconda/bin/conda" create -y -n py310 python=3.10

# 7. Clean up the installer
rm -f "$INSTALLER"

# 8. Success message
echo "Miniconda installed for user '$USER_NAME'."
#echo "Python 3.10 environment 'py310' created."
#echo "To use it, the user should restart the terminal or run: source ~/.bashrc && conda activate py310"
