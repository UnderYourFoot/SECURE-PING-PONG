import socket
import argparse
import json
from crypto_utils import encrypt_message, decrypt_message

parser = argparse.ArgumentParser(description="SecurePing Client")
parser.add_argument('--ip', required=True, help="Server IP")
parser.add_argument('--key', required=True, help="Secret key")
args = parser.parse_args()

# Load config
with open('config.json') as f:
    config = json.load(f)

port = config["port"]

message = "ping"
ciphertext = encrypt_message(args.key, message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((args.ip, port))
    s.sendall(ciphertext)
    data = s.recv(1024)

try:
    plaintext = decrypt_message(args.key, data)
    print("Server responded:", plaintext)
except Exception as e:
    print("Failed to decrypt server response:", e)
