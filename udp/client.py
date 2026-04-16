import socket
import os

SERVER_HOST = os.environ.get("SERVER_HOST", "localhost")
SERVER_PORT = int(os.environ.get("SERVER_PORT", 9000))

text = input("Ingrese un texto: ")

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.settimeout(5)
    s.sendto(text.encode(), (SERVER_HOST, SERVER_PORT))
    try:
        data, _ = s.recvfrom(1024)
        print(f"Respuesta del servidor: {data.decode()}")
    except TimeoutError:
        print("Error: el servidor no respondió en el tiempo esperado.")
