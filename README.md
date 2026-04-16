# RyTD2026-examples

Ejemplos de código para la materia **Redes y Transmisión de Datos**.

---

## Objetivo pedagógico

Este repositorio muestra, con ejemplos mínimos en Python, cómo una aplicación de usuario:

1. construye mensajes de **capa de aplicación** (texto),
2. los entrega a un servicio de **capa de transporte** (TCP o UDP),
3. recibe una respuesta y la presenta al usuario.

En ambos casos (TCP y UDP), la lógica de aplicación es simple: el servidor recibe texto y responde ese texto en mayúsculas.

---

## Ejemplos disponibles

### UDP (`udp/`)

Cliente y servidor en Python usando sockets UDP.  
El cliente envía un texto al servidor; el servidor lo convierte a mayúsculas y lo devuelve.

### TCP (`tcp/`)

Cliente y servidor en Python usando sockets TCP.  
El cliente envía un texto al servidor; el servidor lo convierte a mayúsculas y lo devuelve.

---

## Tecnologías usadas

- **Python 3.12**: lenguaje de programación de los ejemplos.
- **Módulo `socket`** (biblioteca estándar): API para usar servicios de transporte del SO.
- **Docker** (opcional): para ejecutar cliente/servidor en contenedores y simular nodos separados.

---

## Relación con el modelo por capas (enfoque de redes)

### Capa de aplicación (lo que ve el alumno en el programa)

- El mensaje que el usuario escribe con `input(...)`.
- La regla del servicio: convertir texto a mayúsculas.
- Los `print(...)` que muestran solicitud y respuesta.

### Capa de transporte (servicio que usa la aplicación)

- **UDP** (`SOCK_DGRAM`):
  - sin conexión previa,
  - sin garantía de entrega,
  - sin garantía de orden,
  - útil cuando se prioriza simpleza/baja sobrecarga.
- **TCP** (`SOCK_STREAM`):
  - orientado a conexión (handshake),
  - entrega confiable y ordenada,
  - control de flujo y retransmisiones,
  - útil cuando se necesita confiabilidad.

### Qué observar en los ejemplos

- En UDP se usa `sendto/recvfrom` y cada envío es un datagrama independiente.
- En TCP se usa `connect/sendall/recv` sobre una conexión establecida.
- Ambos usan `encode/decode` porque la red transporta **bytes**, no strings de Python.

---

## Ejecución local

Requisitos:

- Python 3.12+ instalado.
- Dos terminales abiertas en la raíz del repositorio.

### UDP

```bash
# Terminal 1 – servidor
python udp/server.py

# Terminal 2 – cliente
python udp/client.py
```

Prueba sugerida:

1. En el cliente escribir: `hola redes`.
2. Verificar que el servidor muestre recepción y envío.
3. Verificar que el cliente reciba: `HOLA REDES`.

### TCP

```bash
# Terminal 1 – servidor
python tcp/server.py

# Terminal 2 – cliente
python tcp/client.py
```

Prueba sugerida:

1. En el cliente escribir: `transporte confiable`.
2. Verificar conexión aceptada en el servidor.
3. Verificar respuesta en mayúsculas en el cliente.

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

---

## Variables de entorno útiles

- `SERVER_HOST`: host o IP del servidor (default: `localhost`).
- `SERVER_PORT`: puerto del servidor (default: `9000`).

Ejemplo local (cliente TCP apuntando a otra IP):

```bash
SERVER_HOST=192.168.1.20 SERVER_PORT=9000 python tcp/client.py
```

---

## Preguntas guía para clase

1. ¿Qué parte del código corresponde a aplicación y cuál a transporte?
2. ¿Qué cambia en el cliente/servidor al pasar de UDP a TCP?
3. ¿Qué problema práctico aparece si en UDP se pierde un datagrama?
4. ¿Por qué en TCP se necesita aceptar conexiones (`accept`)?
5. ¿Qué ventaja/desventaja tiene cada servicio según el tipo de aplicación?
