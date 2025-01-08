# Extend the echo server, which returns to client the data, encrypted using the Caesar cipher algorithm by a specific key 
# obtained from the client.

import socket

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def udp_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"UDP сервер запущено на {host}:{port}")

    while True:
        data, address = server_socket.recvfrom(1024)
        message, shift = data.decode().rsplit(',', 1)
        shift = int(shift)
        encrypted_message = caesar_cipher(message, shift)
        print(f"Отримано дані від {address}: {message} з ключем {shift}")
        server_socket.sendto(encrypted_message.encode(), address)

if __name__ == "__main__":
    udp_server('127.0.0.1', 8888)
