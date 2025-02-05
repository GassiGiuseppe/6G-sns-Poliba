import subprocess
import time
from pathlib import Path
import traci

from daemon import Daemon

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




def omnet_starter():
    sumoCmd = ["sumo-gui", "-c", "your_sumo_config_file.sumocfg"]
    traci.start(sumoCmd)

    step = 0
    while step < 1000:  # Numero di step della simulazione
        traci.simulationStep()
        print(traci.vehicle.getIDList())
        if "veh0" in traci.vehicle.getIDList():  # Controlla se il veicolo esiste
            position = traci.vehicle.getPosition("veh0")
            print(f"Step {step}: Posizione di veh0 -> {position}")
        step += 1

    traci.close()



def main():
    print('hello')
    # preparation()
    omnet_starter()

    

main()