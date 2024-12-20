def hashing(message, hash_val=5381):
    for ch in message:
        # Multiply the current hash by 33 and add the ASCII value of the character
        hash_val = ((hash_val * 33) + ord(ch)) & 0xFFFFFFFF  # Keep within 32-bit range
    return hash_val

hashed = hashing("SindhuVittal")
print(hashed)