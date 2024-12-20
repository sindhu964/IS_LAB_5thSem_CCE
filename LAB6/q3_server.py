import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Create and sign a message using RSA private key
def sign_message(message, private_key):
    h = SHA256.new(message.encode('utf-8'))
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

# Server function
def server():
    # Generate RSA keys for signing
    rsa_key = RSA.generate(2048)
    private_key = rsa_key
    public_key = rsa_key.publickey()

    # Message to be signed
    message = "This is not a message."

    # Sign the message
    signature = sign_message(message, private_key)

    # Create socket and listen for connections
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    print("Server is listening on port 8080...")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    # Send message length first
    conn.sendall(str(len(message)).encode('utf-8') + b'\n')
    
    # Send message
    conn.sendall(message.encode('utf-8'))

    # Send signature length and signature
    conn.sendall(str(len(signature)).encode('utf-8') + b'\n')
    conn.sendall(signature)

    # Send public key
    public_key_bytes = public_key.export_key()
    conn.sendall(str(len(public_key_bytes)).encode('utf-8') + b'\n')
    conn.sendall(public_key_bytes)

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    server()