alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = input('Enter the message to be encrypted : ')
key = input('Enter the key : ')
ct = ''
pt = ''
i=0
j=0
print('ENCRYPTION')
while(i<len(key) and j<len(msg)):
    k = (alpha.index(msg[j]) + alpha.index(key[i]))%26
    ct += alpha[k]
    i = i+1
    j = j+1
    if(i==len(key)):
        i = 0
print(ct)

i=0
j=0
print('\nDECRYPTION')
while(i<len(key) and j<len(ct)):
    k = (alpha.index(ct[j]) - alpha.index(key[i]))%26
    pt += alpha[k]
    i = i+1
    j = j+1
    if(i==len(key)):
        i = 0
print(pt)