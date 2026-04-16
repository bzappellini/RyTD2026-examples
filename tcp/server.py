import socket  # Biblioteca estándar para programación de sockets.
import os  # Biblioteca para leer configuración desde variables de entorno.

HOST = os.environ.get("SERVER_BIND_HOST", "127.0.0.1")  # Host local de escucha (localhost por defecto; configurable para Docker).
PORT = 9000  # Puerto TCP en el que el servidor aceptará conexiones.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Crea un socket IPv4 orientado a conexión (TCP).
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Permite reutilizar el puerto rápidamente tras reiniciar.
    s.bind((HOST, PORT))  # Asocia el socket al host/puerto local del servidor.
    s.listen()  # Pone el socket en modo escucha para aceptar clientes.
    print(f"Servidor TCP escuchando en {HOST}:{PORT}")  # Informa dónde está escuchando el servidor.
    while True:  # Bucle principal: acepta clientes uno por uno.
        conn, addr = s.accept()  # Bloquea hasta recibir una nueva conexión TCP entrante.
        with conn:  # Gestiona la conexión aceptada y la cierra al salir del bloque.
            print(f"Conexión desde {addr}")  # Muestra la dirección IP y puerto del cliente conectado.
            while True:  # Bucle de intercambio de datos con el cliente actual.
                data = conn.recv(1024)  # Recibe hasta 1024 bytes del flujo TCP.
                if not data:  # Si llega vacío, el cliente cerró la conexión.
                    break  # Sale del bucle y vuelve a esperar otro cliente.
                text = data.decode()  # Convierte bytes a texto.
                print(f"Recibido: {text}")  # Log del mensaje recibido.
                response = text.upper()  # Lógica de aplicación: transformar a mayúsculas.
                conn.sendall(response.encode())  # Envía toda la respuesta al cliente por la misma conexión.
                print(f"Enviado: {response}")  # Log de la respuesta enviada.
