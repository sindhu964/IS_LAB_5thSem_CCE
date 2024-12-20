from Crypto.Util.Padding import pad, unpad 
from Crypto.Random import get_random_bytes 

def generate_keypair(p=1024): 
#"""Generates a public/private key pair""" 
    while True: 
        x = int.from_bytes(get_random_bytes(p // 8), byteorder='big') 
        if pow(2, p - 1, p) == 1 and 1 < x < p-1: 
            break 
    g = 2 
    y = pow(g, x, p) 
    return ((p, g, y), x)  # Public key, private key 

def encrypt(pub_key, message): 
#"""Encrypts a message using the public key""" 
    p, g, y = pub_key 
    r = int.from_bytes(get_random_bytes(p // 8), byteorder='big') 
    while math.gcd(r, p) != 1: 
        r = int.from_bytes(get_random_bytes(p // 8), byteorder='big') 
    a = pow(g, r, p) 
    b = (message * pow(y, r, p)) % p 
    return (a, b) 

def decrypt(priv_key, ciphertext): 
#"""Decrypts a ciphertext using the private key""" 
    p, g, _ = priv_key 
    a, b = ciphertext 
    x = priv_key 
    message = (b * pow(a, -x, p)) % p 
    return message 

def homomorphic_comparison(ciphertext1, ciphertext2, pub_key): 
#"""Performs homomorphic comparison on ciphertexts (greater than)""" 
    p, g, y = pub_key 
    a1, b1 = ciphertext1 
    a2, b2 = ciphertext2 
    return (a1 * a2) % p, (b1 * b2 * pow(y, 1, p)) % p  # Encrypted result (m1 > m2) 

# Generate key pair 
pub_key, priv_key = generate_keypair() 
# Blood pressure readings (already encrypted) 
blood_pressure1 = encrypt(pub_key, 120) 
blood_pressure2 = encrypt(pub_key, 140) 
# Homomorphic comparison (encrypted result) 
ciphertext_comparison = homomorphic_comparison(blood_pressure1, blood_pressure2, 
pub_key) 
# Decrypt the comparison result (optional - for demonstration only) 
# decrypted_comparison = decrypt(priv_key, ciphertext_comparison) 
# print(f"Decrypted comparison: {decrypted_comparison} (True if blood pressure 1 > blood 
#pressure 2)") 
# Diagnosis based on the encrypted comparison result 
diagnosis = ciphertext_comparison[0] * pow(ciphertext_comparison[1], -1, pub_key[0]) % pub_key[0] 
if diagnosis > 1: 
    print("Diagnosis: High Blood Pressure detected.") 
else: 
    print("Diagnosis: Normal Blood Pressure.")