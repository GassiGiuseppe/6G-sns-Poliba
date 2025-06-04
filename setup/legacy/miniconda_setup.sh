#!/bin/bash

# Nome dello script: install_miniconda_py37.sh
# Descrizione: Installa Miniconda e crea un ambiente Python 3.7 chiamato py37 su Ubuntu.

# URL per scaricare Miniconda
MINICONDA_URL="https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"
INSTALLER="Miniconda3-latest-Linux-x86_64.sh"

# Funzione per stampare messaggi
function echo_message() {
    echo -e "\n=== $1 ===\n"
}

# 1. Aggiorna e installa i prerequisiti
echo_message "Aggiornamento dei pacchetti di sistema"
sudo apt update && sudo apt upgrade -y
sudo apt install -y curl bzip2

# 2. Scarica Miniconda
echo_message "Scaricamento dell'installer di Miniconda"
curl -o $INSTALLER $MINICONDA_URL

# 3. Installa Miniconda
echo_message "Installazione di Miniconda"
bash $INSTALLER -b -p $HOME/miniconda

# 4. Inizializza Miniconda
echo_message "Inizializzazione di Miniconda"
eval "$($HOME/miniconda/bin/conda shell.bash hook)"
conda init

# 5. Crea un ambiente con Python 3.7
echo_message "Creazione dell'ambiente 'py37' con Python 3.7"
conda create -y -n py37 python=3.7

# 6. Attiva l'ambiente creato
echo_message "Attivazione dell'ambiente 'py37'"
conda activate py37

# 7. Pulizia (rimuove l'installer)
echo_message "Pulizia dei file temporanei"
rm $INSTALLER

echo_message "Installazione e configurazione completate!"
echo "Per iniziare a usare l'ambiente, esegui: conda activate py37"
