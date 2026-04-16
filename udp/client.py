import socket  # Biblioteca para crear y usar sockets.
import os  # Biblioteca para leer variables de entorno.

SERVER_HOST = os.environ.get("SERVER_HOST", "localhost")  # Host del servidor, configurable por variable de entorno.
SERVER_PORT = int(os.environ.get("SERVER_PORT", 9000))  # Puerto del servidor, configurable y convertido a entero.

text = input("Ingrese un texto: ")  # Captura desde teclado el mensaje de aplicación que se quiere enviar.

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Crea un socket UDP sobre IPv4.
    s.settimeout(5)  # Define un tiempo máximo de espera (5 s) para evitar bloqueo infinito.
    s.sendto(text.encode(), (SERVER_HOST, SERVER_PORT))  # Envía el mensaje en bytes al servidor remoto.
    try:  # Intenta recibir una respuesta del servidor.
        data, _ = s.recvfrom(1024)  # Espera un datagrama de respuesta de hasta 1024 bytes.
        print(f"Respuesta del servidor: {data.decode()}")  # Decodifica e imprime la respuesta recibida.
    except TimeoutError:  # Si no llega respuesta dentro del timeout, se maneja el error.
        print("Error: el servidor no respondió en el tiempo esperado.")  # Informa al usuario el problema de comunicación.
