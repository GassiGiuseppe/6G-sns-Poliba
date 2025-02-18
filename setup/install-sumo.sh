cd /home/$SUDO_USER
curl -L -O https://sumo.dlr.de/releases/1.6.0/sumo-src-1.6.0.tar.gz
tar -xzvf sumo-src-1.6.0.tar.gz 
cd ./sumo-1.6.0
mkdir build/cmake-build && cd build/cmake-build
cmake ../..
make -j$(nproc)
exit 0