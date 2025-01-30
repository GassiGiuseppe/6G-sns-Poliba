import subprocess
import time
from pathlib import Path

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





def main():
    
    preparation()

    

main()