# it is the real daemon 

from pathlib import Path
import time
import yaml
import threading

class Daemon:

    def __init__(self, log_id):
        self._QUEUE = []
        self._QUEUE_LOCK = threading.Lock()

        file_path = yaml.safe_load(open(Path('code/settings.yml')))[log_id]
        file_path = Path(file_path)
        self._file_path = file_path

        # create the thread daemon but not start it
        self._tail_thread = threading.Thread(target=self._tail_f, args=(self._file_path,))
        self._tail_thread.daemon = True

        self._line_cursor = 0
    
    def start(self):
        self._tail_thread.start()


    def _tail_f(self, file_path):
        # method similar to tail -f that monitorates file changes in real time 
        # with r is not blocking the file
        with open(file_path, 'r') as file:
            # end of file
            file.seek(0, 2)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue

                with self._QUEUE_LOCK:
                    self._QUEUE.append(line)


    def get_next_line(self):
        while True:
            with self._QUEUE_LOCK:
                if len(self._QUEUE)> self._line_cursor:
                    self._line_cursor = self._line_cursor + 1
                    return self._QUEUE[self._line_cursor - 1].strip()
                # debug phase
                #if i == 28:
                #    print(QUEUE)