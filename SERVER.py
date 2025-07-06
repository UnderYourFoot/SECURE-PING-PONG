import socket
import json
from crypto_utils import decrypt_message, encrypt_message

# Load config
with open('config.json') as f:
    config = json.load(f)

secret_key = config["secret_key"]
port = config["port"]

HOST = '0.0.0.0'  # Listen on all interfaces

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, port))
    s.listen()
    print(f"SecurePing server listening on port {port}...")
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        data = conn.recv(1024)
        if data:
            try:
                message = decrypt_message(secret_key, data)
                if message == "ping":
                    print("Valid ping received!")
                    response = encrypt_message(secret_key, "pong")
                    conn.sendall(response)
                else:
                    print("Invalid message.")
            except Exception as e:
                print("Decryption failed:", e)
