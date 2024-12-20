#Using socket programming in Python, demonstrate the application of hash functions for ensuring data integrity during transmission over a network. Write server and client scripts where the server computes the hash of received data and sends it back to the client, which then verifies the integrity of the data by comparing the received hash with the locally computed hash. Show how the hash verification detects data corruption or tampering during transmission.

import socket
import hashlib

# Function to compute the SHA-256 hash of the received data
def compute_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def start_server():
    # Server setup
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("Server listening on port 9999...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")

        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break
        print(f"Data received: {data.decode()}")

        # Compute the hash of the received data
        data_hash = compute_hash(data)
        print(f"Computed hash: {data_hash}")

        # Send the computed hash back to the client
        conn.sendall(data_hash.encode())
        conn.close()

if __name__ == "__main__":
    start_server()