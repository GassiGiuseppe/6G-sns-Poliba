#!/bin/bash

# Nome dello script: install_miniconda_py37.sh
# Descrizione: Installa Miniconda e crea un ambiente Python 3.7 chiamato py37 su Ubuntu, da eseguire con sudo.

# URL per scaricare Miniconda
MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
INSTALLER="Miniconda3-latest-Linux-x86_64.sh"

# Ottieni l'utente originale che ha eseguito sudo
USER_HOME=$(eval echo ~${SUDO_USER})
USER_NAME=$SUDO_USER

# 1. Aggiorna e installa i prerequisiti
apt update && apt upgrade -y
apt install -y curl bzip2

# 2. Scarica Miniconda
curl -o $INSTALLER $MINICONDA_URL

# 3. Installa Miniconda
bash $INSTALLER -b -p $USER_HOME/miniconda

# 4. Inizializza Miniconda
eval "$($USER_HOME/miniconda/bin/conda shell.bash hook)"
sudo -u $USER_NAME bash -c "$USER_HOME/miniconda/bin/conda init"

# 5. Crea un ambiente con Python 3.7
sudo -u $USER_NAME bash -c "$USER_HOME/miniconda/bin/conda create -y -n py310 python=3.10"

# 6. Pulizia (rimuove l'installer)
rm $INSTALLER

# 7. Messaggio finale
echo "Per iniziare a usare l'ambiente, esegui: conda activate py310"