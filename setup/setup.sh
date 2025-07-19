#!/bin/bash

# Impostare frontend non interattivo per apt
export DEBIAN_FRONTEND=noninteractive

# Rileva la directory dello script
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Aggiornare il sistema e installare i pacchetti richiesti
sudo apt update && sudo apt upgrade -y && \
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

# Creare la directory di lavoro nella home dell'utente
WORKSPACE="/home/$SUDO_USER"
cd "$WORKSPACE"

# Configurare le variabili d'ambiente
# sudo -u $USER export SUMO_HOME="$WORKSPACE/artifacts/sumo-1.6.0"
SUMO_HOME="$WORKSPACE/sumo-1.6.0"

# Modificare .bashrc per la persistenza
BASHRC_PATH="/home/$SUDO_USER/.bashrc"
#sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/omnetpp-5.6/bin' >> $BASHRC_PATH"
#sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin' >> $BASHRC_PATH"
#sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:/root/miniforge3/condabin' >> $BASHRC_PATH"
#sudo -u $SUDO_USER bash -c "echo 'export SUMO_HOME=$WORKSPACE/sumo-1.6.0' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export GDK_BACKEND=x11' >> $BASHRC_PATH"

# Applicare le modifiche immediatamente nella shell corrente dell'utente
#sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/omnetpp-5.6/bin"
#sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin"
#sudo -u $SUDO_USER bash -c "export PATH=\$PATH:/root/miniforge3/condabin"
#sudo -u $SUDO_USER bash -c "export SUMO_HOME=$WORKSPACE/sumo-1.6.0"
sudo -u $SUDO_USER bash -c "export GDK_BACKEND=x11"

# Installare SUMO
sh "$SCRIPT_DIR/install-omnet.sh"
#sh "$SCRIPT_DIR/install-sumo.sh"
sudo -u "$SUDO_USER" bash "$SCRIPT_DIR/install-sumo.sh"



# Installare Miniforge (alternativa a conda)
# sh "$SCRIPT_DIR/install-miniforge.sh"
# install vscode
sh "$SCRIPT_DIR/vscode.sh"
# install conda
sh "$SCRIPT_DIR/sudo_miniconda_setup.sh"

# Installazione di Omnet con opp_env
#   credo lo spazio per nix
mkdir -m 0755 /nix
chown "$SUDO_USER" /nix
sudo -u "$SUDO_USER" bash -c "bash install_opp_env.sh"

# Informare e riavviare il sistema
echo "Setup completato. Il sistema si riavvierà tra 10 secondi..."
sleep 10
reboot

