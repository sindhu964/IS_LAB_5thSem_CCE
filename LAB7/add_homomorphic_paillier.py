from Crypto.PublicKey import RSA 
from Crypto.Random import get_random_bytes 
import math
from phe import paillier

def generate_keypair(nlength=1024): 
#Generates a public/private key pair""" 
    key = RSA.generate(nlength) 
    pub_key = key.publickey() 
    return pub_key, key 

def encrypt(pub_key, message): 
#"""Encrypts a message using the public key""" 
    random_bytes = get_random_bytes(16) 
    p, q = pub_key.n // 2, pub_key.n // 2 + 1 
    while math.gcd(p, q) != 1: 
        p, q = pub_key.n // 2, pub_key.n // 2 + 1 
    m_dot = pow(message, 2, pub_key.n) 
    r_dot = pow(int.from_bytes(random_bytes, byteorder='big'), 2, pub_key.n) 
    ciphertext = m_dot * r_dot % pub_key.n 
    return ciphertext 

def decrypt(priv_key, ciphertext): 
#"""Decrypts a ciphertext using the private key""" 
    p = priv_key.n // 2 
    l = (ciphertext - 1) // pub_key.n 
    message = math.floor(l * pow(p, -1, priv_key.n)) 
    return message 

def homomorphic_add(ciphertext1, ciphertext2, pub_key): 
#"""Performs homomorphic addition on ciphertexts""" 
    return ciphertext1 * ciphertext2 % pub_key.n 

# Generate key pair 
pub_key, priv_key = generate_keypair() 
# Encrypt integers 
a = 5 
b = 10 
ciphertext_a = encrypt(pub_key, a) 
ciphertext_b = encrypt(pub_key, b) 
# Homomorphic addition 
ciphertext_sum = homomorphic_add(ciphertext_a, ciphertext_b, pub_key) 
# Decrypt the sum (optional) 
#decrypted_sum = decrypt(priv_key, ciphertext_sum) 
#print(f"Decrypted sum: {decrypted_sum}") 
print(f"Ciphertext of a: {ciphertext_a}") 
print(f"Ciphertext of b: {ciphertext_b}") 
print(f"Ciphertext of a + b: {ciphertext_sum}") 