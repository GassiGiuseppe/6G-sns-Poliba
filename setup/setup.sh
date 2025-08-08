#!/bin/bash
set -euo pipefail

# Set non-interactive frontend for apt to avoid prompts
export DEBIAN_FRONTEND=noninteractive

# Get the absolute path to the directory containing this script
SCRIPT_DIR="$(dirname "$(realpath "$0")")"

# Update the system and install required packages
sudo apt update && sudo apt upgrade -y
sudo apt install -y \
  git curl wget make cmake build-essential g++ gcc clang lld gdb \
  bison flex perl python3 python3-dev python3-pip \
  qt5-qmake qtbase5-dev libqt5opengl5-dev \
  libxml2-dev zlib1g-dev \
  openscenegraph libopenscenegraph-dev libosgearth-dev \
  libgeos-dev libgdal-dev libproj-dev \
  libglew-dev libzip-dev libcurl4-gnutls-dev \
  doxygen graphviz \
  libxerces-c-dev libfox-1.6-dev libgl2ps-dev \
  swig libxrandr-dev libzmq3-dev \
  protobuf-compiler \
  default-jre openjdk-11-jdk \
  libboost-all-dev \
  openmpi-bin libopenmpi-dev

# Set user and workspace directory
USER="${SUDO_USER:-$USER}"
WORKSPACE="/home/$USER"
cd "$WORKSPACE"

# Set SUMO environment variable
# SUMO_HOME="$WORKSPACE/sumo-1.6.0"
BASHRC_PATH="$WORKSPACE/.bashrc"

# Append required environment variable to .bashrc
sudo -u "$USER" bash -c "echo 'export GDK_BACKEND=x11' >> \"$BASHRC_PATH\""

# Run setup scripts
sh "$SCRIPT_DIR/install-omnet.sh"
sh "$SCRIPT_DIR/install-sumo.sh"
sh "$SCRIPT_DIR/vscode.sh"
sh "$SCRIPT_DIR/sudo_miniconda_setup.sh"

# Create /nix directory with correct permissions
mkdir -m 0755 /nix
chown "$USER" /nix

# Run the opp_env setup as the target user
sudo -u "$USER" bash "$SCRIPT_DIR/wip/install_opp_env.sh"

# Reboot after setup
echo "Setup completed. System will reboot in 10 seconds..."
sleep 10
reboot
