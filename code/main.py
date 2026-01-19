import subprocess
import time
from pathlib import Path
import traci
# from sumolib.miscutils import getFreeSocketPort
import sumolib
import os
#import 
import struct

# from omnet_launcher import launch_ini_as_process
from opp_env_launcher import launch_ini_as_process
from sumo_launcher import launch_sumo

def starter():

    launch_ini_as_process()
    print("ini process launched")
    launch_sumo()
    print("sumo launched")

    step = 0
    print('waiting for other')


    while traci.simulation.getMinExpectedNumber == 0:
        time.sleep(1)
    
    step = 0
    while step < 1000:  # Numero di step della simulazione
        traci.simulationStep()
        print(traci.vehicle.getIDList())
        if "veh0" in traci.vehicle.getIDList():  # Controlla se il veicolo esiste
            position = traci.vehicle.getPosition("veh0")
            #print(f"Step {step}: Posizione di veh0 -> {position}")

        step += 1

    traci.close()



def main():
    print('hello')
    # preparation()
    # sumo_thread = 
    starter()
    # right_starter()
    #sumo_starter()    

    
# execute this code in your terminal, not in the ide nor vscode
main()
