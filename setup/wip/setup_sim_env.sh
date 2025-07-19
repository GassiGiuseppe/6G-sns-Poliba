
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
if opp_env info &>/dev/null; then
  echo "Workspace opp_env già esistente in $SIM_ENV_DIR, salto init"
else
  echo "Inizializzo nuovo workspace opp_env"
  opp_env init
fi

# Installa i framework richiesti
echo "Installazione INET..."
opp_env install inet-latest

echo "Installazione Simu5G..."
opp_env install simu5g-latest

echo "Installazione Veins (incluso Veins_INET)..."
opp_env install veins-latest

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
echo "Ora puoi lanciare omnetpp digitando: omnetpp"
