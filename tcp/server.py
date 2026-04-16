import socket

HOST = "0.0.0.0"
PORT = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Servidor TCP escuchando en {HOST}:{PORT}")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Conexión desde {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                text = data.decode()
                print(f"Recibido: {text}")
                response = text.upper()
                conn.sendall(response.encode())
                print(f"Enviado: {response}")
