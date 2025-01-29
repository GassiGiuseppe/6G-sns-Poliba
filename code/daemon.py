from pathlib import Path
import time
import yaml
import threading

QUEUE = []
QUEUE_LOCK = threading.Lock()

def tail_f(file_path):
    # function similar to tail -f that monitorates file changes in real time 

    # with r is not blocking the file
    with open(file_path, 'r') as file:
        # end of file
        file.seek(0, 2)
        
        while True:
            line = file.readline()
            
            if not line:
                time.sleep(0.1)
                continue
            
            with QUEUE_LOCK:
                QUEUE.append(line)


def print_queue():
    i = 0
    while True:
        with QUEUE_LOCK:
            if len(QUEUE)>i:
                print(QUEUE[i])
                i = i + 1
                

def main():
    
    file_path = yaml.safe_load(open(Path('code/settings.yml')))['log_file']
    file_path = Path(file_path)

    tail_thread = threading.Thread(target=tail_f, args=(file_path,))
    tail_thread.daemon = True
    tail_thread.start()

    print_queue()



main()
