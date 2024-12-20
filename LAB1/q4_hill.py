import numpy as np

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = input('Enter the message to be encrypted : ').lower().replace(' ','')
key = np.array([[3,3],[2,7]])

if len(msg)%2 !=0 :
    msg += 'x'
p = [alpha.index(letter) for letter in msg]
p = np.reshape(p, (-1, 2))
#print(p)
#msg_inv = np.linalg.inv(p)

print("ENCRYPTION")
ct_matrix = (np.dot(p,key))%26
#print(ct_matrix)
ct = "".join(alpha[num] for num in ct_matrix.flatten())
print(ct)

print("\nDECRYPTION\n")
key_inv = np.linalg.inv(key)
print(key_inv%26)
