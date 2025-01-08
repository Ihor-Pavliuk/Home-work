import socket

def udp_client(host, port, message, shift):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    combined_message = f"{message},{shift}"
    client_socket.sendto(combined_message.encode(), (host, port))
    
    data, server = client_socket.recvfrom(1024)
    print(f"Отримано відповідь від сервера: {data.decode()}")

if __name__ == "__main__":
    udp_client('127.0.0.1', 8888, "Привіт, сервер!", 4)
