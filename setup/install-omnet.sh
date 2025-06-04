cd /home/$SUDO_USER/
curl -L -O https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.6/omnetpp-5.6-src-linux.tgz
tar -xvzf ./omnetpp-5.6-src-linux.tgz
cd ./omnetpp-5.6 

# 
sudo -u $SUDO_USER bash -c "export PATH=/home/$SUDO_USER/omnetpp-5.6.2/bin:\$PATH"


# give the user the correct right over the files
chown -R $SUDO_USER:$SUDO_USER /home/$SUDO_USER/omnetpp-5.6.2
chmod -R 775 /home/$SUDO_USER/omnetpp-5.6.2

# does the command to compile 
sudo -u $SUDO_USER bash -c -i "
. /home/$SUDO_USER/omnetpp-5.6.2/setenv && 
cd /home/$SUDO_USER/omnetpp-5.6.2 && 
./configure && 
make"

# sudo -u $SUDO_USER . setenv
# sudo -u $SUDO_USER ./configure
# sudo -u $SUDO_USER make

exit 0
