cd /workspace/artifacts
curl -L -O https://github.com/omnetpp/omnetpp/releases/download/omnetpp-5.6/omnetpp-5.6-src-linux.tgz
tar -xvzf ./omnetpp-5.6-src-linux.tgz
cd ./omnetpp-5.6 
./configure
make
exit 0