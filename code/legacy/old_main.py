import subprocess
import time
from pathlib import Path
import traci
# from sumolib.miscutils import getFreeSocketPort
import sumolib
import os
from code.legacy.daemon import Daemon
#import 
import struct

from omnet_launcher import launch_ini_as_process
from sumo_launcher import launch_sumo

TEST = True

def preparation():

    # daemon_path = Path('code/daemon.py')
    # subprocess.Popen(["python", daemon_path])


    if TEST:
        # adversarial is used only in test phase
        adversarial_path = Path('code/adversarial.py')
        subprocess.Popen(["python", adversarial_path])

    daemon = Daemon('log_file')
    daemon.start()

    
    for _ in range(30):
        print(daemon.get_next_line())



def cmd_file_send():
    file_path = "../../prova/simulations/heterogeneous.sumocfg"
    #with open(file_path, "rb") as f:
    #	file_data = f.read()
    
    #return file_data

def sumo_starter():
    sumoCmd = ["sumo", "-c", "../../prova/simulations/heterogeneous.sumocfg"]
    traci.start(sumoCmd)

def omnet_starter():
    # sumoCmd = ["sumo-gui", "-c", "../../prova/simulations/heterogeneous.sumocfg"]
    # traci.start(sumoCmd)
    os.chdir('../../prova/simulations')
    # PORT = sumolib.miscutils.getFreeSocketPort()
    traci.start(["sumo", "-c", "heterogeneous.sumocfg", "--num-clients", "2"], port = 9999)
    

    
    # print(PORT)
    #def drl_execution():
    # traci.init(port=9999)
    
    # cmd file send
    # conn = traci.getConnection()
    # file_data = cmd_file_send()
    # message = struct.pack("!Bi", 0x75, len(file_data)) + file_data
    # traci.connection._sendExact()
    # conn._sendRaw(message)
    # responde = traci.connection._recvExact()
    # print("risposta:", responde)
    # end cmd file send
    
    traci.setOrder(2)
    step = 0
    print('waiting for other')
    #while traci.simulation.getMinExpectedNumber == 0:
    #	time.sleep(1)
    
    print('ci sono auto')
    input("clicca un tasto per far partire la simulazione")
    while step < 1000:  # Numero di step della simulazione
        traci.simulationStep()
        print(traci.vehicle.getIDList())
        if "veh0" in traci.vehicle.getIDList():  # Controlla se il veicolo esiste
            position = traci.vehicle.getPosition("veh0")
            #print(f"Step {step}: Posizione di veh0 -> {position}")

        step += 1

    traci.close()


def right_starter():
    traci.init(port=9999)
    traci.setOrder(2)
    step = 0
    print('waiting for other')
    #while traci.simulation.getMinExpectedNumber == 0:
    #	time.sleep(1)
    
    # print('hello')
    print('ci sono auto')
    while step < 1000:  # Numero di step della simulazione
        traci.simulationStep()
        print(traci.vehicle.getIDList())
        if "veh0" in traci.vehicle.getIDList():  # Controlla se il veicolo esiste
            position = traci.vehicle.getPosition("veh0")
            #print(f"Step {step}: Posizione di veh0 -> {position}")
        step += 1

    traci.close()
    
    

def starter():

    launch_ini_as_process()
    print("ini process launched")
    launch_sumo()
    print("sumo launched")
    #os.chdir('../../prova/simulations')
    # traci.start(["sumo", "-c", "heterogeneous.sumocfg", "--num-clients", "2"], port = 9999)
    # now i start the ini simulation
    # launch_ini()
    # end
    
    # traci.setOrder(2)
    step = 0
    print('waiting for other')
    """"
    while traci.simulation.getMinExpectedNumber == 0:
    	    time.sleep(1)
    """

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

    

main()
