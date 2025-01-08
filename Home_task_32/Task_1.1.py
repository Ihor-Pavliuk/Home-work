# During the lesson, we have created a server and client, which use TCP/IP protocol for communication via sockets. 
# In this task, you have to create a server and client, which will use user datagram protocol (UDP) for communication

import socket

def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP сервер запущено на {host}:{port}")

    while True:
        data, address = server_socket.recvfrom(1024)
        print(f"Отримано дані від {address}: {data.decode()}")
        server_socket.sendto(data, address)

if __name__ == "__main__":
    udp_server('127.0.0.1', 8888)
