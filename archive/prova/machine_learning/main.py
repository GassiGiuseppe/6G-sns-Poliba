import socket

def start_server(host='127.0.0.1', port=12345):
        
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)
        
        conn, addr = server_socket.accept()
        
        try:
            while True:
                data = conn.recv(1024)
                if data:
                    print(f"Messaggio: {data.decode('utf-8')}")
                    # close connection and establish a new one
                    conn.close()
                    server_socket.close()
                    
                    server_socket.bind((host, port))
                    server_socket.listen(1)
                    conn, addr = server_socket.accept()
                #    break
                    
                
        
        except KeyboardInterrupt:
            print('chiusura del server')
        finally:
            conn.close()
            server_socket.close()
            
start_server()
