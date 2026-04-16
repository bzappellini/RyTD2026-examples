import socket
import os

SERVER_HOST = os.environ.get("SERVER_HOST", "localhost")
SERVER_PORT = int(os.environ.get("SERVER_PORT", 9000))

text = input("Ingrese un texto: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERVER_HOST, SERVER_PORT))
    s.sendall(text.encode())
    data = s.recv(1024)
    print(f"Respuesta del servidor: {data.decode()}")
