import hashlib
import random
from Crypto.Util import number

# Key Generation for Schnorr Signature
def generate_schnorr_keys(key_size=256):
    # Generate a large prime p and a generator g (where q is a prime divisor of p-1)
    p = number.getPrime(key_size)
    q = number.getPrime(key_size // 2)
    g = pow(2, (p - 1) // q, p)  # Generator g
    
    # Private key x: Random number from 1 to q-1
    private_key = random.randint(1, q - 1)
    
    # Public key y: y = g^x mod p
    public_key = pow(g, private_key, p)
    
    return (p, q, g, public_key), private_key  # Public key (p, q, g, y) and private key x

# Hash the message using SHA-256
def hash_message(message):
    return int(hashlib.sha256(message.encode('utf-8')).hexdigest(), 16)

# Schnorr Signature Generation
def schnorr_sign(private_key, message, p, q, g):
    # Hash the message
    h = hash_message(message)
    
    # Choose a random k from 1 to q-1
    k = random.randint(1, q - 1)
    
    # Compute r = g^k mod p
    r = pow(g, k, p)
    
    # Compute e = H(r || message)
    e = hash_message(str(r) + message) % q
    
    # Compute s = (k + e * private_key) mod q
    s = (k + e * private_key) % q
    
    return (r, s)

# Schnorr Signature Verification
def schnorr_verify(public_key, message, signature, p, q, g):
    r, s = signature
    h = hash_message(message)
    
    # Compute e = H(r || message)
    e = hash_message(str(r) + message) % q
    
    # Compute g^s mod p and (y^e * r) mod p
    left_hand_side = pow(g, s, p)
    right_hand_side = (pow(public_key, e, p) * r) % p
    
    # Check if g^s mod p == y^e * r mod p
    return left_hand_side == right_hand_side

# Example Usage
def main():
    message = "This is a test"
    
    # Generate Schnorr public and private keys
    public_key, private_key = generate_schnorr_keys()
    p, q, g, y = public_key
    
    print(f"Public Key: (p={p}, q={q}, g={g}, y={y})")
    print(f"Private Key: {private_key}")
    
    # Sign the message
    signature = schnorr_sign(private_key, message, p, q, g)
    print(f"Signature: {signature}")
    
    # Verify the signature
    is_valid = schnorr_verify(y, message, signature, p, q, g)
    if is_valid:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")

if __name__ == "__main__":
    main()