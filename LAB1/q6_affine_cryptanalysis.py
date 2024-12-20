import string
import math

# Affine cipher encryption function
def affine_encrypt(plaintext, a, b):
    alphabet = string.ascii_uppercase
    encrypted_text = ''
    
    # Encrypt each letter
    for ch in plaintext.upper():
        if ch in alphabet:
            x = ord(ch) - ord('A')  # Convert letter to number
            # Apply the encryption formula: E(x) = (a * x + b) % 26
            encrypted_num = (a * x + b) % 26
            encrypted_text += chr(encrypted_num + ord('A'))
        else:
            encrypted_text += ch  # Keep non-alphabet characters unchanged
    
    return encrypted_text

# Check if a number is coprime with 26
def is_coprime(a):
    return math.gcd(a, 26) == 1

# Brute-force attack to find the key
def find_affine_key(plaintext, ciphertext):
    possible_a_values = [a for a in range(1, 26) if is_coprime(a)]
    possible_b_values = range(26)
    
    for a in possible_a_values:
        for b in possible_b_values:
            encrypted = affine_encrypt(plaintext, a, b)
            if encrypted == ciphertext:
                return a, b
    return None, None

# Known plaintext-ciphertext pair
plaintext = "ab"
ciphertext = "GL"

# Find the key using brute-force
a, b = find_affine_key(plaintext, ciphertext)

# Display the found key
if a is not None and b is not None:
    print(f"Found key: a = {a}, b = {b}")
else:
    print("Key not found.")