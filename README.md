# SecurePing

SecurePing es un proyecto sencillo para probar conceptos de ciberseguridad y comunicación entre dispositivos. Permite que dispositivos en la misma red local intercambien “pings” cifrados y solo respondan si conocen una clave compartida.

Ideal para aprender:
- Autenticación básica
- Criptografía simétrica (AES)
- Programación de sockets
- Seguridad en redes locales

## Cómo funciona

- **Cliente** envía un mensaje “ping” cifrado al servidor.
- **Servidor** descifra el mensaje y, si la clave es correcta, responde con un “pong” (XD) cifrado.
- Dispositivos desconocidos (sin la clave) no reciben respuesta útil.

## Requisitos

- Python 3
- cryptography

Instalación:
```bash
pip install cryptography

pip install server.py

python client.py --ip <IP_DEL_SERVIDOR> --key MiClaveSecreta



