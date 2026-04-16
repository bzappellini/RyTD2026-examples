# RyTD2026-examples

Ejemplos de código para la materia **Redes y Transmisión de Datos**.

---

## Ejemplos disponibles

### UDP (`udp/`)

Cliente y servidor en Python usando sockets UDP.  
El cliente envía un texto al servidor; el servidor lo convierte a mayúsculas y lo devuelve.

### TCP (`tcp/`)

Cliente y servidor en Python usando sockets TCP.  
El cliente envía un texto al servidor; el servidor lo convierte a mayúsculas y lo devuelve.

---

## Ejecución local

### UDP

```bash
# Terminal 1 – servidor
python udp/server.py

# Terminal 2 – cliente
python udp/client.py
```

### TCP

```bash
# Terminal 1 – servidor
python tcp/server.py

# Terminal 2 – cliente
python tcp/client.py
```

---

## Ejecución con Docker

El cliente acepta la variable de entorno `SERVER_HOST` para apuntar al servidor por nombre o IP.  
El servidor siempre escucha en el puerto **9000**.

### UDP

```bash
# Construir imágenes
docker build -f udp/Dockerfile.server -t udp-server ./udp
docker build -f udp/Dockerfile.client -t udp-client ./udp

# Correr servidor (máquina A)
docker run --rm -p 9000:9000/udp udp-server

# Correr cliente (máquina B) apuntando al servidor por nombre o IP
docker run --rm -it -e SERVER_HOST=<nombre-o-ip-del-servidor> udp-client
```

### TCP

```bash
# Construir imágenes
docker build -f tcp/Dockerfile.server -t tcp-server ./tcp
docker build -f tcp/Dockerfile.client -t tcp-client ./tcp

# Correr servidor (máquina A)
docker run --rm -p 9000:9000 tcp-server

# Correr cliente (máquina B) apuntando al servidor por nombre o IP
docker run --rm -it -e SERVER_HOST=<nombre-o-ip-del-servidor> tcp-client
```
