# Echo server with threading

# Create a socket echo server which handles each connection in a separate Thread

import  socket, threading


def connection_threads(connection, addr):
        with connection:
            print(f"Connected with Client({addr})")
            while True:
                print
                data = connection.recv(1024)
                if not data:
                    break
                print(f"receive {data.decode()} from {addr}")
            connection.sendall(f"Server response {data.decode()}".encode())

def start_server_tcp(host="127.0.0.1", port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: # UDP
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Socket listening on {host}:{port}")
        while True:
            connection, addr = server_socket.accept()
            thread = threading.Thread(target=connection_threads, args=(connection, addr), name=f"ClientThread-{addr}")
            thread.start()
            



if __name__ == "__main__":
    start_server_tcp()

