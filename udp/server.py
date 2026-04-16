import socket

HOST = "0.0.0.0"  # Escucha en todas las interfaces (necesario en Docker)
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print(f"Servidor UDP escuchando en {HOST}:{PORT}")
    while True:
        data, addr = s.recvfrom(1024)
        text = data.decode()
        print(f"Recibido de {addr}: {text}")
        response = text.upper()
        s.sendto(response.encode(), addr)
        print(f"Enviado a {addr}: {response}")
