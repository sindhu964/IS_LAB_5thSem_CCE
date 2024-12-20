import socket   
import hashlib

# Function to compute the SHA-256 hash of the data
def compute_hash(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()

def start_client(data_to_send):
    # Client setup
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    # Send data to the server
    client_socket.sendall(data_to_send.encode())

    # Receive the hash from the server
    server_hash = client_socket.recv(1024).decode()
    print(f"Hash received from server: {server_hash}")

    # Compute the local hash
    local_hash = compute_hash(data_to_send.encode())
    print(f"Locally computed hash: {local_hash}")

    # Verify if the hashes match
    if local_hash == server_hash:
        print("Data integrity verified: No corruption detected.")
    else:
        print("Data corruption or tampering detected!")

    client_socket.close()

if __name__ == "__main__":
    data_to_send = "This is the message to verify data integrity."
    start_client(data_to_send)