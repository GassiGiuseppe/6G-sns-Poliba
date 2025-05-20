import os
import subprocess
import time
from multiprocessing import Process
# in this file we will try to launch the ini file
# the ini file is the configuration file of omnet's section of the project

def launch_ini():
    time.sleep(5)

    absolute_path = '/home/simu5g/simu5g-workspace/prova/simulations/omnetpp.ini'   # of the ini file

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
    subprocess.run(["pwd"])
    r = subprocess.run(command)

def launch_ini_as_process():
    p = Process(target=launch_ini)
    p.daemon = True
    p.start()

# launch_ini()
