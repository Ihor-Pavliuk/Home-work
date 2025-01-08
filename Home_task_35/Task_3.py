# Echo server with multiprocessing

# Create a socket echo server that handles each connection using the multiprocessing library.

import socket
import multiprocessing

def handle_client(connection, address):
    print(f"Connection from {address}")
    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"Received {data} from {address}")
        connection.sendall(data)
    connection.close()

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server started at {host}:{port}")
    while True:
        connection, address = server_socket.accept()
        process = multiprocessing.Process(target=handle_client, args=(connection, address))
        process.start()
        connection.close()

if __name__ == "__main__":
    start_server('127.0.0.1', 8888)
