import socket  # Biblioteca estándar para trabajar con sockets de red.

HOST = "0.0.0.0"  # Escucha en todas las interfaces de red de la máquina.
PORT = 9000  # Puerto UDP donde este proceso quedará esperando datagramas.

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:  # Crea un socket IPv4 (AF_INET) de tipo UDP (SOCK_DGRAM).
    s.bind((HOST, PORT))  # Asocia el socket a la IP/puerto local para poder recibir mensajes.
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")  # Muestra en consola dónde está escuchando el servidor.
    while True:  # Bucle infinito para atender múltiples mensajes de distintos clientes.
        data, addr = s.recvfrom(1024)  # Espera un datagrama de hasta 1024 bytes y obtiene también la dirección del emisor.
        text = data.decode()  # Convierte los bytes recibidos en texto usando UTF-8 por defecto.
        print(f"Recibido de {addr}: {text}")  # Registra quién envió el mensaje y su contenido.
        response = text.upper()  # Lógica de aplicación: transformar el texto a mayúsculas.
        s.sendto(response.encode(), addr)  # Envía la respuesta al mismo host/puerto desde donde llegó el mensaje.
        print(f"Enviado a {addr}: {response}")  # Confirma en consola qué respuesta se envió.
