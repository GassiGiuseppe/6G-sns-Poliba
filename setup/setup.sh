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

# Creare la directory di lavoro
WORKSPACE="/workspace"
mkdir -p "$WORKSPACE/artifacts/install-scripts"
cd "$WORKSPACE"

# Configurare le variabili d'ambiente
export SUMO_HOME="$WORKSPACE/artifacts/sumo-1.6.0"
echo "export PATH=\$PATH:$WORKSPACE/artifacts/omnetpp-5.6/bin" >> ~/.bashrc
echo "export PATH=\$PATH:$WORKSPACE/artifacts/sumo-1.6.0/bin" >> ~/.bashrc
echo "export PATH=\$PATH:/root/miniforge3/condabin" >> ~/.bashrc
echo "export SUMO_HOME=$SUMO_HOME" >> ~/.bashrc
echo "export GDK_BACKEND=x11" >> ~/.bashrc

# Applica immediatamente le modifiche al profilo corrente
source ~/.bashrc

# Installare OMNeT++ e SUMO
sh "$SCRIPT_DIR/install-omnet.sh"
sh "$SCRIPT_DIR/install-sumo.sh"

# Installare Miniforge (obbligatorio)
sh "$SCRIPT_DIR/install-miniforge.sh"

# Informare e riavviare il sistema
echo "Setup completato. Il sistema si riavvierà tra 10 secondi..."
sleep 10
# reboot
