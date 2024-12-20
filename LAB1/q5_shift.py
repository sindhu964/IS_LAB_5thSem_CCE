import string

# Shift cipher decryption function
def shift_decrypt(ciphertext, shift):
    alphabet = string.ascii_uppercase
    decrypted_text = ''
    
    # Decrypt each letter
    for ch in ciphertext:
        if ch in alphabet:
            y = alphabet.index(ch)
            # Apply the decryption formula: D(y) = (y - shift) % 26
            decrypted_num = (y - shift) % 26
            decrypted_text += alphabet[decrypted_num]
        else:
            decrypted_text += ch  # Keep non-alphabet characters unchanged
    
    return decrypted_text

# Calculate the shift using known plaintext-ciphertext pair
def find_shift(plain, cipher):
    plain_num = [ord(ch) - ord('a') for ch in plain]
    cipher_num = [ord(ch) - ord('A') for ch in cipher]
    # Calculate the shift by comparing plaintext and ciphertext
    shift = (cipher_num[0] - plain_num[0]) % 26
    return shift

# Known plaintext-ciphertext pair
plain_text = "yes"
cipher_pair = "CIW"

# Find the shift
shift_value = find_shift(plain_text, cipher_pair)

# Ciphertext to decrypt
ciphertext = "XVIEWYWI"

# Decrypt the ciphertext using the found shift
decrypted_message = shift_decrypt(ciphertext, shift_value)
print("Decrypted message:", decrypted_message)