#!/bin/bash
# Install SUMO 1.6.0 from source and set up environment variables

set -euo pipefail

# Define user and workspace
USER="${SUDO_USER:-$USER}"
SUMO_VERSION="1.6.0"
WORKSPACE="/home/$USER"

echo "SUMO $SUMO_VERSION is installing"

# Change to user workspace
cd "$WORKSPACE"

# Download and extract SUMO source
curl -L -O "https://sumo.dlr.de/releases/${SUMO_VERSION}/sumo-src-${SUMO_VERSION}.tar.gz"
tar -xzvf "sumo-src-${SUMO_VERSION}.tar.gz"
rm "sumo-src-${SUMO_VERSION}.tar.gz"

# Build SUMO
cd "sumo-${SUMO_VERSION}"
mkdir -p build/cmake-build
cd build/cmake-build
cmake ../..
make -j"$(nproc)"

# Add SUMO to PATH and set SUMO_HOME in .bashrc
{
  echo "export PATH=\$PATH:$WORKSPACE/sumo-${SUMO_VERSION}/bin"
  echo "export SUMO_HOME=$WORKSPACE/sumo-${SUMO_VERSION}"
} >> "$WORKSPACE/.bashrc"

echo "SUMO $SUMO_VERSION installed and environment variables set."
exit 0
