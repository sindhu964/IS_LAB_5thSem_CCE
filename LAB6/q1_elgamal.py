import hashlib
import random
from Crypto.Util import number

# Generate ElGamal keys
def generate_elgamal_keys(key_size=256):
    # Generate a large prime p and a generator g
    p = number.getPrime(key_size)
    g = random.randint(2, p - 1)
    
    # Private key x, random number from 1 to p-2
    x = random.randint(1, p - 2)
    
    # Public key y = g^x mod p
    y = pow(g, x, p)
    
    return (p, g, y), x  # Public key (p, g, y) and private key x

# Hash message using SHA-256
def hash_message(message):
    return int(hashlib.sha256(message.encode('utf-8')).hexdigest(), 16)

# ElGamal Signature Generation
def elgamal_sign(private_key, message, p, g):
    # Hash the message
    h = hash_message(message)
    
    # Choose random k where 1 <= k <= p-2 and gcd(k, p-1) = 1
    while True:
        k = random.randint(1, p - 2)
        if number.GCD(k, p - 1) == 1:
            break
    
    # r = g^k mod p
    r = pow(g, k, p)
    
    # s = (h - x*r) * k^(-1) mod (p-1)
    k_inv = number.inverse(k, p - 1)  # Modular inverse of k mod (p-1)
    s = (k_inv * (h - private_key * r)) % (p - 1)
    
    return (r, s)

# ElGamal Signature Verification
def elgamal_verify(public_key, message, signature):
    p, g, y = public_key
    r, s = signature
    h = hash_message(message)
    
    # Check if r is valid
    if not (0 < r < p):
        return False
    
    # Verify the signature
    v1 = pow(y, r, p) * pow(r, s, p) % p
    v2 = pow(g, h, p)
    
    return v1 == v2

# Example Usage
def main():
    message = "This is a secret message"
    
    # Generate ElGamal public and private keys
    public_key, private_key = generate_elgamal_keys()
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Sign the message
    signature = elgamal_sign(private_key, message, public_key[0], public_key[1])
    print(f"Signature: {signature}")
    
    # Verify the signature
    is_valid = elgamal_verify(public_key, message, signature)
    if is_valid:
        print("Signature is valid.")
    else:
        print("Signature is invalid.")

if __name__ == "__main__":
    main()