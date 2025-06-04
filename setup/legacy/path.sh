WORKSPACE="/home/$SUDO_USER/workspace"

# Modificare .bashrc per la persistenza
BASHRC_PATH="/home/$SUDO_USER/.bashrc"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/omnetpp-5.6.2/bin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export PATH=\$PATH:/root/miniforge3/condabin' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export SUMO_HOME=$WORKSPACE/sumo-1.6.0' >> $BASHRC_PATH"
sudo -u $SUDO_USER bash -c "echo 'export GDK_BACKEND=x11' >> $BASHRC_PATH"

# Applicare le modifiche immediatamente nella shell corrente dell'utente
# source sarebbe un'alternativa a quanto segue
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/omnetpp-5.6.2/bin"
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:$WORKSPACE/sumo-1.6.0/bin"
sudo -u $SUDO_USER bash -c "export PATH=\$PATH:/root/miniforge3/condabin"
sudo -u $SUDO_USER bash -c "export SUMO_HOME=$WORKSPACE/sumo-1.6.0"
sudo -u $SUDO_USER bash -c "export GDK_BACKEND=x11"
