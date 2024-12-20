import random
from sympy import isprime

# Generate a large prime number of given bit size
def generate_large_prime(bits=256):
    return next(n for n in iter(lambda: random.getrandbits(bits), None) if isprime(n))

# Diffie-Hellman key generation function
def dh_keygen(bits=256):
    # Generate a prime number p and a generator g
    p = generate_large_prime(bits)
    g = random.randint(2, p - 2)

    # Private keys for both parties
    a = random.randint(1, p - 2)  # Private key of party A
    b = random.randint(1, p - 2)  # Private key of party B

    # Public keys to be exchanged
    A = pow(g, a, p)  # A's public key
    B = pow(g, b, p)  # B's public key

    # Shared secrets (should be the same for both parties)
    shared_secret_A = pow(B, a, p)  # A's computed shared secret
    shared_secret_B = pow(A, b, p)  # B's computed shared secret

    return (p, g, A, B), (shared_secret_A, shared_secret_B)

# Running the key generation and shared secret computation
(pub, (sec_A, sec_B)) = dh_keygen()

# Output results
print("Public values (p, g, A, B):", *pub)
print("Shared secrets match?", sec_A == sec_B)