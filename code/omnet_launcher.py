import os
import subprocess
import time
from multiprocessing import Process
# in this file we will try to launch the ini file
# the ini file is the configuration file of omnet's section of the project

def launch_ini():
    time.sleep(5)

    # absolute_path = '/home/utente/Desktop/prova/prova/simulations/omnetpp.ini'   # of the ini file
    absolute_path = '/home/utente/6G-sns-Poliba/archive/prova/simulations/omnetpp.ini'

    # <-- exemple of the command -->
    final_commmand = '../src/prova_dbg -m -u Qtenv -n .:../src:../../inet4.4/examples:../../inet4.4/showcases:../../inet4.4/src:../../inet4.4/tests/validation:../../inet4.4/tests/networks:../../inet4.4/tutorials:../../simu5G/emulation:../../simu5G/simulations:../../simu5G/src:../../veins_inet/src/veins_inet:../../veins_inet/examples/veins_inet:../../veins-veins-5.2/examples/veins:../../veins-veins-5.2/src/veins -x inet.common.selfdoc;inet.linklayer.configurator.gatescheduling.z3;inet.showcases.visualizer.osg;inet.transportlayer.tcp_lwip;inet.showcases.emulation;inet.applications.voipstream;inet.visualizer.osg;inet.examples.voipstream --image-path=../../inet4.4/images:../../simu5G/images:../../veins_inet/images:../../veins-veins-5.2/images -l ../../inet4.4/src/INET -l ../../simu5G/src/simu5g -l ../../veins_inet/src/veins_inet -l ../../veins-veins-5.2/src/veins omnetpp.i'

    """

    -n .:../src:../../inet4.4/examples:../../inet4.4/showcases:../../inet4.4/src:../../inet4.4/tests/validation:../../inet4.4/tests/networks:../../inet4.4/tutorials:../../simu5G/emulation:../../simu5G/simulations:../../simu5G/src:../../veins_inet/src/veins_inet:../../veins_inet/examples/veins_inet:../../veins-veins-5.2/examples/veins:../../veins-veins-5.2/src/veins
    -x inet.common.selfdoc;inet.linklayer.configurator.gatescheduling.z3;inet.showcases.visualizer.osg;inet.transportlayer.tcp_lwip;inet.showcases.emulation;inet.applications.voipstream;inet.visualizer.osg;inet.examples.voipstream 
    --image-path=../../inet4.4/images:../../simu5G/images:../../veins_inet/images:../../veins-veins-5.2/images 
    -l ../../inet4.4/src/INET 
    -l ../../simu5G/src/simu5g 
    -l ../../veins_inet/src/veins_inet 
    -l ../../veins-veins-5.2/src/veins 
    omnetpp.i


    """

    enviroment = "Cmdenv" # it can be Qtenv or Cmdenv, at the beginning it needs the flag -u

    # from the absolute path we build the working directory and the file name

    working_dir = os.path.dirname(absolute_path)
    file_name = os.path.basename(absolute_path)

    # now we move to the working dir to execute the command
    os.chdir(working_dir)

    """
    command = [
        "../src/prova_dbg", # executable of the simulation
        "-m",               # multiple modality
        "-u", "Qtenv",      # user interface
        # ned files needed
        "-n", ".:../src:../../inet4.4/examples:../../inet4.4/showcases:../../inet4.4/src:../../inet4.4/tests/validation:../../inet4.4/tests/networks:../../inet4.4/tutorials:../../simu5G/emulation:../../simu5G/simulations:../../simu5G/src:../../veins_inet/src/veins_inet:../../veins_inet/examples/veins_inet:../../veins-veins-5.2/examples/veins:../../veins-veins-5.2/src/veins",
        # modules to exlude from simulation
        "-x", "inet.common.selfdoc;inet.linklayer.configurator.gatescheduling.z3;inet.showcases.visualizer.osg;inet.transportlayer.tcp_lwip;inet.showcases.emulation;inet.applications.voipstream;inet.visualizer.osg;inet.examples.voipstream",
        # images
        "--image-path", "../../inet4.4/images:../../simu5G/images:../../veins_inet/images:../../veins-veins-5.2/images",
        #
        "-l", "../../inet4.4/src/INET",
        "-l", "../../simu5G/src/simu5g",
        "-l", "../../veins_inet/src/veins_inet",
        "-l", "../../veins-veins-5.2/src/veins",
        #
        "omnetpp.ini"
    ]
    """
    command = [
        "../../../../opp_workspaces/simu5g-env/omnetpp-6.0.3/bin/opp_run_dbg",
        "-m",
        "-u", "Qtenv",

        # NED paths
        "-n",
        "..:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/examples:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/showcases:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/src:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/validation:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/tests/networks:"
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/tutorials:"
        "../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/emulation:"
        "../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/simulations:"
        "../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src:"
        "../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet:"
        "../../../../opp_workspaces/simu5g-env/veins_inet/examples/veins_inet:"
        "../../../../opp_workspaces/simu5g-env/veins-5.3/examples/veins:"
        "../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins",

        # Excluded modules
        "-x",
        "inet.common.selfdoc;"
        "inet.emulation;"
        "inet.showcases.visualizer.osg;"
        "inet.examples.emulation;"
        "inet.showcases.emulation;"
        "inet.visualizer.osg",

        # Image paths
        "--image-path",
        "../../../../opp_workspaces/simu5g-env/inet-4.4.2/images:"
        "../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/images:"
        "../../../../opp_workspaces/simu5g-env/veins_inet/images:"
        "../../../../opp_workspaces/simu5g-env/veins-5.3/images",

        # Shared libraries
        "-l", "../../../../opp_workspaces/simu5g-env/inet-4.4.2/src/INET",
        "-l", "../../../../opp_workspaces/simu5g-env/simu5g-1.2.1/src/simu5g",
        "-l", "../../../../opp_workspaces/simu5g-env/veins_inet/src/veins_inet",
        "-l", "../../../../opp_workspaces/simu5g-env/veins-5.3/src/veins",

        # INI file
        "omnetpp.ini"
    ]

    subprocess.run(["pwd"])
    r = subprocess.run(command)

def launch_ini_as_process():
    p = Process(target=launch_ini)
    p.daemon = True
    p.start()

# launch_ini()
