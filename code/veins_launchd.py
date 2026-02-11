#!/usr/bin/env python3
import os
import sys
import socket
import select
import subprocess
import logging
import optparse
import time

# Versione aggiornata per supporto Multi-Client (Python + Veins)
# Ispirata alle implementazioni di co-simulazione OpenCAMS [2]

def run_sumo(sumo_cmd, num_clients, remote_port, runpath):
    """Lancia SUMO con il numero di client specificato."""
    # Costruisce il comando includendo --num-clients
    cmd = sumo_cmd.split()
    cmd.extend(["--remote-port", str(remote_port)])
    if num_clients > 1:
        cmd.extend(["--num-clients", str(num_clients)])
    
    logging.info(f"Esecuzione: {' '.join(cmd)} sulla porta {remote_port}")
    
    # Avvio del processo
    return subprocess.Popen(cmd, cwd=runpath)

def proxy_traffic(client_socket, sumo_port):
    """Gestisce il proxying dei messaggi TraCI tra Veins e SUMO."""
    sumo_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sumo_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    
    # Retry per attendere che SUMO apra il socket
    for _ in range(10):
        try:
            sumo_socket.connect(("127.0.0.1", sumo_port))
            break
        except socket.error:
            time.sleep(0.5)
    
    sockets = [client_socket, sumo_socket]
    while True:
        ins, _, _ = select.select(sockets,,)
        for s in ins:
            data = s.recv(4096)
            if not data: return
            out = sumo_socket if s is client_socket else client_socket
            out.sendall(data)

def main():
    parser = optparse.OptionParser()
    parser.add_option("-c", "--command", dest="command", default="sumo", help="comando SUMO")
    parser.add_option("-p", "--port", dest="port", type="int", default=9999, help="porta di ascolto daemon")
    parser.add_option("-n", "--num-clients", dest="num_clients", type="int", default=1, help="numero di client totali attesi da SUMO")
    parser.add_option("-v", "--verbose", action="count", dest="verbose", default=0)
    options, args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if options.verbose else logging.INFO)
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", options.port))
    server_socket.listen(5)
    logging.info(f"Daemon in ascolto sulla porta {options.port}...")

    while True:
        client_conn, addr = server_socket.accept()
        logging.info(f"Connessione ricevuta da {addr}")
        
        # In una simulazione reale, qui si leggerebbe il file XML di setup
        # Per semplicità in questo script usiamo parametri diretti.
        
        sumo_proc = run_sumo(options.command, options.num_clients, options.port + 1, os.getcwd())
        try:
            proxy_traffic(client_conn, options.port + 1)
        finally:
            logging.info("Chiusura simulazione.")
            sumo_proc.terminate()
            client_conn.close()

if __name__ == "__main__":
    main()
