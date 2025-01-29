import socket
import queue
import threading
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

LOG_FILE = "log.txt"
HOST = "localhost"
PORT = 5000

log_queue = queue.Queue()


class LogHandler(FileSystemEventHandler):
    """Gestisce i cambiamenti del file di log."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r")
        self.file.seek(0, 2)  # Sposta il cursore alla fine del file

    def on_modified(self, event):
        """Viene chiamato quando il file viene modificato."""
        if event.src_path == self.file_path:
            line = self.file.readline()
            if line:
                log_queue.put(line.strip())


def start_file_watcher():
    """Avvia l'osservatore per il file di log."""
    event_handler = LogHandler(LOG_FILE)
    observer = Observer()
    observer.schedule(event_handler, path=".", recursive=False)
    observer.start()
    try:
        while True:
            pass  # Mantiene il thread attivo
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def start_server():
    """Avvia un server socket che invia il prossimo elemento della coda."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen()

        print("Server in ascolto...")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                if not log_queue.empty():
                    conn.sendall(log_queue.get().encode())
                else:
                    conn.sendall(b"QUEUE EMPTY")


if __name__ == "__main__":
    threading.Thread(target=start_file_watcher, daemon=True).start()
    start_server()
