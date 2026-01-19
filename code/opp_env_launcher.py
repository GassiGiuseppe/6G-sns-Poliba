import os
import subprocess
import time
from multiprocessing import Process

OPP_ENV_WORKSPACE = "/home/utente/opp_workspaces/simu5g-env"
SIMULATION_DIR = "/home/utente/6G-sns-Poliba/archive/prova/simulations"
INI_FILE = "omnetpp.ini"

def launch_ini():
    time.sleep(1)

    os.chdir(OPP_ENV_WORKSPACE)

    # Single-line command for opp_env run -c
    # command_1 = 'cd /home/utente/6G-sns-Poliba/archive/prova/simulations'
    # command_2 = 'opp_run -m -u Qtenv -n ..:../../../../opp_workspaces/simu5g-env/inet-4.4.2/examples:../../../../opp_workspaces/simu5g-env/inet-4.4.2/showcases:../../../../opp_workspaces/simu5g-env/inet-4.4.2/src:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/validation:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/networks:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tutorials:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/emulation:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/simulations:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src:../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet:../../../../opp_workspaces/simu5g-env/veins_inet/examples/veins_inet:../../../../opp_workspaces/simu5g-env/veins-5.3/examples/veins:../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins -x "inet.common.selfdoc;inet.emulation;inet.showcases.visualizer.osg;inet.examples.emulation;inet.showcases.emulation;inet.visualizer.osg" --image-path=../../../../opp_workspaces/simu5g-env/inet-4.4.2/images:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/images:../../../../opp_workspaces/simu5g-env/veins_inet/images:../../../../opp_workspaces/simu5g-env/veins-5.3/images -l ../../../../opp_workspaces/simu5g-env/inet-4.4.2/src/INET -l ../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src/simu5g -l ../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet -l ../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins omnetpp.ini'
    # command = '"' + command_1 + ' && ' + command_2 + '"'
    # command = '"pwd"'

    command_str = (
        f'cd {SIMULATION_DIR} && opp_run -m -u Qtenv '
        f'-n .:../../../../opp_workspaces/simu5g-env/inet-4.4.2/examples:../../../../opp_workspaces/simu5g-env/inet-4.4.2/showcases:../../../../opp_workspaces/simu5g-env/inet-4.4.2/src:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/validation:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/networks:../../../../opp_workspaces/simu5g-env/inet-4.4.2/tutorials:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/emulation:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/simulations:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src:../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet:../../../../opp_workspaces/simu5g-env/veins_inet/examples/veins_inet:../../../../opp_workspaces/simu5g-env/veins-5.3/examples/veins:../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins '
        f'-x "inet.common.selfdoc;inet.emulation;inet.showcases.visualizer.osg;inet.examples.emulation;inet.showcases.emulation;inet.visualizer.osg" '
        f'--image-path ../../../../opp_workspaces/simu5g-env/inet-4.4.2/images:../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/images:../../../../opp_workspaces/simu5g-env/veins_inet/images:../../../../opp_workspaces/simu5g-env/veins-5.3/images '
        f'-l ../../../../opp_workspaces/simu5g-env/inet-4.4.2/src/INET '
        f'-l ../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src/simu5g '
        f'-l ../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet '
        f'-l ../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins '
        f'{INI_FILE}'
    )

    # Run opp_env with -c
    # print("command:", " ".join(["opp_env", "run", "-c", command]))
    #subprocess.run(["opp_env", "run", "-c", command], check=True, shell=True)

    subprocess.run(["opp_env", "run", "-c", command_str])

def launch_ini_as_process():
    p = Process(target=launch_ini)
    p.daemon = True
    p.start()
