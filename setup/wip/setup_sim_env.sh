
#!/usr/bin/env bash
set -euo pipefail

# Directory esterna ai repository git
BASE_DIR="$HOME/opp_workspaces"
SIM_ENV_DIR="$BASE_DIR/simu5g-env"

# Crea cartelle
mkdir -p "$SIM_ENV_DIR"
cd "$SIM_ENV_DIR"

# Inizializza opp_env
echo "Creazione ambiente opp_env in: $SIM_ENV_DIR"
# check 
if opp_env info &>/dev/null && [ -d ".metadata" ];then
  # if there is opp_env and the directory of metadata
  echo "Workspace opp_env già esistente in $SIM_ENV_DIR, salto init"
  opp_env init
else
  echo "Inizializzo nuovo workspace opp_env"
  opp_env init
fi

# required: omnet 6.0 , inet 4.4, veins-veins 5.2 , veins-inet, simu5g
# Installa i framework richiesti
# echo "Installing omnetpp 6.0 ..."
# opp_env install omnetpp-6.0.3

# echo "Installazione INET..."
# opp_env install inet-4.4.0  #idk it seems that veins 5.2 prefer inet 4.2.8

# echo "Installazione Veins (incluso Veins_INET)..."
# opp_env install veins-5.3

#e cho "Installazione Simu5G..."
# opp_env install simu5g-1.2.2

# echo "Installazione Veins (incluso Veins_INET)..."
# opp_env install veins-5.3

###################################
# the following mess is because simu5g and veins both want to use different version of omnet and veins

# Install Simu5G and Veins 5.3 (auto-selects OMNeT++ 6.0.3)
echo ">>> Installing Simu5G and Veins 5.3"
opp_env install simu5g-1.2.2 veins-5.3



#####################################

# Crea script di attivazione
echo "Creazione script activate.sh"
cat <<EOF > activate.sh
#!/usr/bin/env bash
source "\$(dirname "\$0")/shell"
EOF
chmod +x activate.sh

# Crea wrapper in ~/.local/bin
WRAPPER_PATH="$HOME/.local/bin/omnetpp"
mkdir -p "$HOME/.local/bin"

echo "Creazione wrapper omnetpp in $WRAPPER_PATH"
cat <<EOF > "$WRAPPER_PATH"
#!/usr/bin/env bash
source "$SIM_ENV_DIR/shell"
exec omnetpp "\$@"
EOF
chmod +x "$WRAPPER_PATH"

# Controlla se ~/.local/bin è nel PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
  echo 'Attenzione: ~/.local/bin non è nel PATH. Aggiungilo con:'
  echo '  echo "export PATH=\$HOME/.local/bin:\$PATH" >> ~/.bashrc && source ~/.bashrc'
fi

echo "Ambiente creato in '$SIM_ENV_DIR'"
echo "Framework installati: INET, Simu5G, Veins (con Veins_INET)"
#echo "Ora puoi lanciare omnetpp digitando: omnetpp"
