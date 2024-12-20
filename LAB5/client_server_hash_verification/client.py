import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Function to verify a signed message using RSA public key
def verify_signature(message, signature, public_key):
    try:
        h = SHA256.new(message.encode('utf-8'))
        pkcs1_15.new(public_key).verify(h, signature)
        print("Signature is valid.")
    except (ValueError, TypeError):
        print("Signature is invalid!")

# Client function
def client():
    # Create socket to connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Receive the message length
    message_len = int(client_socket.recv(1024).decode('utf-8').strip())

    # Receive the actual message
    message = client_socket.recv(message_len).decode('utf-8')

    # Receive the signature length
    signature_len = int(client_socket.recv(1024).decode('utf-8').strip())

    # Receive the signature
    signature = client_socket.recv(signature_len)

    # Receive the public key length
    public_key_len = int(client_socket.recv(1024).decode('utf-8').strip())

    # Receive the public key
    public_key_data = client_socket.recv(public_key_len)
    public_key = RSA.import_key(public_key_data)

    # Verify the received signature
    verify_signature(message, signature, public_key)

    client_socket.close()

if _name_ == "_main_":
    client()