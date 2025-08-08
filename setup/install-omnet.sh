#!/bin/bash

# Determina l'utente vero
USER="${SUDO_USER:-$USER}"
WORKSPACE=$(eval echo "~$USER")
OMNET_VERSION="5.6"
OMNET_DIR="$WORKSPACE/omnetpp-$OMNET_VERSION"
TARBALL="omnetpp-$OMNET_VERSION-src-linux.tgz"
URL="https://github.com/omnetpp/omnetpp/releases/download/omnetpp-$OMNET_VERSION/$TARBALL"

# Scarica ed estrai OMNeT++
cd "$WORKSPACE" || exit 1
curl -L -O "$URL"
tar -xvzf "$TARBALL"
rm "$TARBALL"

# Modifica il .bashrc PRIMA della compilazione
BASHRC="$WORKSPACE/.bashrc"
LINE="export PATH=\$PATH:$OMNET_DIR/bin"

# Evita duplicazioni
grep -qxF "$LINE" "$BASHRC" || echo "$LINE" >> "$BASHRC"

# Dai i permessi all’utente normale
chown -R "$USER:$USER" "$OMNET_DIR"
chmod -R 775 "$OMNET_DIR"

# Compila come utente non-root con shell interattiva per caricare .bashrc
sudo -u "$USER" bash -i <<EOF
cd "$OMNET_DIR"
. ./setenv
./configure
make
EOF

exit 0
