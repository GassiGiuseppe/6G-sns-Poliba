#USER_HOME="/home/${SUDO_USER:-$USER}" #rindondante con workspace
SUMO_VERSION="1.6.0"
WORKSPACE="/home/$SUDO_USER"
cd "$WORKSPACE"
#cd /home/$SUDO_USER
curl -L -O https://sumo.dlr.de/releases/1.6.0/sumo-src-1.6.0.tar.gz
tar -xzvf sumo-src-1.6.0.tar.gz 
rm sumo-src-1.6.0.tar.gz 
cd ./sumo-1.6.0
mkdir build/cmake-build && cd build/cmake-build
cmake ../..
make -j$(nproc)
# update bashrc for sumo
echo "export PATH=\$PATH:$USER_HOME/sumo-$SUMO_VERSION/bin" >> "$WORKSPACE/.bashrc"
echo "export SUMO_HOME=$USER_HOME/sumo-$SUMO_VERSION" >> "$WORKSPACE/.bashrc"
exit 0
