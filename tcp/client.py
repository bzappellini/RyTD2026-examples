import socket  # Biblioteca de sockets para comunicación de red.
import os  # Biblioteca para leer configuración desde variables de entorno.

SERVER_HOST = os.environ.get("SERVER_HOST", "localhost")  # Host/IP del servidor TCP (por defecto localhost).
SERVER_PORT = int(os.environ.get("SERVER_PORT", 9000))  # Puerto del servidor convertido a entero.

text = input("Ingrese un texto: ")  # Mensaje de aplicación ingresado por el usuario.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Crea un socket TCP sobre IPv4.
    s.connect((SERVER_HOST, SERVER_PORT))  # Realiza el handshake TCP con el servidor remoto.
    s.sendall(text.encode())  # Envía el mensaje convertido a bytes.
    data = s.recv(1024)  # Espera hasta 1024 bytes de respuesta del servidor.
    print(f"Respuesta del servidor: {data.decode()}")  # Decodifica e imprime la respuesta final.
