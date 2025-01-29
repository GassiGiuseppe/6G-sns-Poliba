import subprocess
import time
from pathlib import Path

TEST = True

def preparation():

    daemon_path = Path('code/daemon.py')
    subprocess.Popen(["python", daemon_path])

    if TEST:
        # adversarial is used only in test phase
        adversarial_path = Path('code/adversarial.py')
        subprocess.Popen(["python", adversarial_path])



def main():
    
    preparation()

    

main()