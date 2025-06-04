#!/bin/bash

# Impostare frontend non interattivo per apt
export DEBIAN_FRONTEND=noninteractive

# Rileva la directory dello script
SCRIPT_DIR=$(dirname "$(realpath "$0")")

# Aggiornare il sistema e installare i pacchetti richiesti
apt update && apt upgrade -y && \
apt install -y \
    git \
    curl \
    make \
    gcc \
    g++ \
    bison \
    flex \
    qt5-qmake \
    qtcreator \
    qtbase5-dev \
    openscenegraph \
    libopenscenegraph-dev \
    libgeos-dev \
    nano \
    cmake \
    libglew-dev \
    libzip-dev \
    zipcmp \
    zipmerge \
    ziptool \
    libcurl4-gnutls-dev \
    libgdal-dev \
    libosgearth-dev \
    build-essential perl \
    python python3 \
    libqt5opengl5-dev tcl-dev tk-dev \
    libxml2-dev zlib1g-dev default-jre doxygen graphviz \
    openjdk-21-jdk \
    libxerces-c-dev libfox-1.6-dev \
    libproj-dev libgl2ps-dev swig libxrandr-dev \
    pip \
    protobuf-compiler \
    wget \
    libzmq3-dev

# Creare la directory di lavoro nella home dell'utente
WORKSPACE="/home/$SUDO_USER"
echo "$WORKSPACE/install-scripts"
mkdir -p "$WORKSPACE/install-scripts"
cd "$WORKSPACE"

# Configurare le variabili d'ambiente
# sudo -u $USER export SUMO_HOME="$WORKSPACE/artifacts/sumo-1.6.0"
SUMO_HOME="$WORKSPACE/sumo-1.6.0"

# Modificare .bashrc per la persistenza
BASHRC_PATH="/home/$SUDO_USER/.bashrc"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/omnetpp-5.6.2/bin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:/root/miniforge3/condabin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export SUMO_HOME=$WORKSPACE/sumo-1.6.0' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export GDK_BACKEND=x11' >> $BASHRC_PATH"

# Applicare le modifiche immediatamente nella shell corrente dell'utente
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/omnetpp-5.6.2/bin"
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin"
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:/root/miniforge3/condabin"
sudo -u $SUDO_USER bash -c "export SUMO_HOME=$WORKSPACE/sumo-1.6.0"
sudo -u $SUDO_USER bash -c "export GDK_BACKEND=x11"

# Installare OMNeT++ e SUMO
sh "$SCRIPT_DIR/install-omnet.sh"
sh "$SCRIPT_DIR/install-sumo.sh"

# Installare Miniforge (obbligatorio)
sh "$SCRIPT_DIR/install-miniforge.sh"

# Informare e riavviare il sistema
echo "Setup completato. Il sistema si riavvierà tra 10 secondi..."
sleep 10
reboot

