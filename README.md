# 6G-sns-Poliba
py 3.9 +


### Installation (Linux)

To install the project, open your terminal and run the following commands:

```bash
# Clone the repository
git clone https://github.com/GassiGiuseppe/6G-sns-Poliba.git
# Navigate to the setup directory
cd 6G-sns-Poliba/setup
# Make the setup script executable
chmod +x setup.sh
# Run the setup script
sudo ./setup.sh
```
## After the setup
Right now this things have to be done by hand, later will be automated
```bash
# go into the folder where your project is located
cd /home/utente/opp_workspaces/simu5g-env
# open opp_env shell
opp_env shell
# rebuild all the project (sometimes cross dependencies may borke otherwise)
clean_all && build_omnetpp && build_inet && build_veins
# then you may open the ide inside opp_env shell
omnetpp
```
Here we need to import inet, then veins ( subproject copied into the env ), then adjust for each of the the properties and build all. (veins-inet3 will not work and that is ok because is deprecated)
After add to the project simu5g, and add to its properties veins, inet and veins-inet, then build.
In the end add your project and adjust its properties, then build again.
(NOTE maybe there is not the need to all of this build but this worked for me)
## Additional 
### TraciLaunchD issue
Veins is currently developing its multi-client traci system, right now is just an experimental features and each version can have some flaws. 
You may need to change how the file "veins-5.3/src/veins/modules/mobility/traci/TraCIScenarioManagerLaunchd.cc" works. In my case the init_traci method expected sumo configuration even if it was not the one to handle it in this case, i just commented everything after the last #endif leaving only the call to its submethod TraCIScenarioManager::init_traci();
(NOTE that this is because even in this multi-client system veins wants still to handle sumo, this in the future may not be a problem and our code can change to let it handle itself)
### SUMO version does not work
if its the case then you should use the sumo shipped with veins, to do so:
```bash
# go into the folder where your project is located
cd /home/utente/opp_workspaces/simu5g-env
# enter into opp_env shell
opp_env shell
# search for nix's sumo path
which sumo
```
then use that path into the python file sumo_launcher.py
NOTE: "opp_env run -c sumo" in the project path will actually execute veins sumo. if this does not cause any problems, we can move on with this choiche instead

