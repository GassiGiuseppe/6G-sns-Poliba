import os
import traci


def launch_sumo():
    os.chdir('/home/utente/6G-sns-Poliba/archive/prova/simulations/')
    # since both python and omnet are connected to sumo, it needs 2 clients
    traci.start(["sumo", "-c", "heterogeneous.sumocfg", "--num-clients", "2"], port = 9999)
    traci.setOrder(2)