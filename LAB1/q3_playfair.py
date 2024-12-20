def create_playfair_matrix(key):
    # Remove duplicates from key and create the matrix with the remaining alphabet
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    key = "".join(sorted(set(key), key=key.index))
    
    for char in key:
        if char not in matrix:
            matrix.append(char)
    
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_encipher(pair, matrix):
    r1, c1 = find_position(matrix, pair[0])
    r2, c2 = find_position(matrix, pair[1])

    if r1 == r2:
        return matrix[r1][(c1 + 1) % 5] + matrix[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return matrix[(r1 + 1) % 5][c1] + matrix[(r2 + 1) % 5][c2]
    else:
        return matrix[r1][c2] + matrix[r2][c1]

def prepare_text(text):
    text = text.upper().replace("J", "I").replace(" ", "")
    prepared_text = ""
    
    i = 0
    while i < len(text):
        prepared_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text += 'X'
            i += 1
        else:
            if i + 1 < len(text):
                prepared_text += text[i + 1]
            i += 2
    
    if len(prepared_text) % 2 != 0:
        prepared_text += 'X'
    
    return prepared_text

def playfair_cipher(text, key):
    matrix = create_playfair_matrix(key)
    prepared_text = prepare_text(text)
    ciphertext = ""
    
    for i in range(0, len(prepared_text), 2):
        ciphertext += playfair_encipher(prepared_text[i:i + 2], matrix)
    
    return ciphertext

# Input
text = "The key is hidden under the door pad"
key = "GUIDANCE"

# Encipher the text
ciphertext = playfair_cipher(text, key)
print("Ciphertext:", ciphertext)
















#Playfair Cipher
def get_array_index(matrix,ch):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(matrix[i][j]==ch):
                return i,j
    return -1          

def create_matrix(key):
    key=key.casefold()
    matrix = []
    alphabet = 'abcdefghiklmnopqrstuvwxyz' #excluding j in since it is less 
    for i in range(5):
        row = []
        for j in range(5):
            if key:
                row.append(key[0])
                alphabet=alphabet.replace(key[0],"")
                key=key.replace(key[0],"")
            else:
                row.append(alphabet[0])
                alphabet=alphabet.replace(alphabet[0],"")
        matrix.append(row)
    return matrix

def encrypt_playfair(message,matrix):
    encrypted_message=""
    message=message.casefold()
    message=message.replace(" ","")
    if(len(message)%2!=0):
        message+='x'
    message=message.replace('j','i') #We can take the j as an i since we ignored it pehle
    for i in range(0,len(message),2):
        a,b = get_array_index(matrix,message[i])
        c,d = get_array_index(matrix,message[i+1])
        if(a==c):
            encrypted_message+=matrix[a][(b+1)%5]
            encrypted_message+=matrix[a][(d+1)%5]
        elif(b==d):
            encrypted_message+=matrix[(a+1)%5][b]
            encrypted_message+=matrix[(c+1)%5][d]
        else:
            encrypted_message+=matrix[a][d]
            encrypted_message+=matrix[c][b]
    return encrypted_message
        
def decrypt_playfair(message,matrix):
    decrypted_message=""
    for i in range(0,len(message),2):
        a,b = get_array_index(matrix,message[i])
        c,d = get_array_index(matrix,message[i+1])
        if(a==c):
            decrypted_message+=matrix[a][(b-1)%5]
            decrypted_message+=matrix[a][(d-1)%5]
        elif(b==d):
            decrypted_message+=matrix[(a-1)%5][b]
            decrypted_message+=matrix[(c-1)%5][d]
        else:
            decrypted_message+=matrix[a][d]
            decrypted_message+=matrix[c][b]
    return decrypted_message        


matrix = create_matrix("GUIDANCE")
print(matrix)
message = "The key is hidden under the door pad"
encrypted_message = encrypt_playfair(message,matrix)
print(encrypted_message)
decrypted_message=decrypt_playfair(encrypted_message, matrix)
print(decrypted_message)