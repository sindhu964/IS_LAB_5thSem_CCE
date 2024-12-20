alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = input('Enter the message to be encrypted : ')
key = input('Enter the key : ')
ct = ''
pt = ''
i=0
j=0
l=0
print('ENCRYPTION')
while(i<len(key) or j<len(msg)):
    if(i==len(key)):
        k = (alpha.index(msg[j]) + alpha.index(msg[l]))%26
        l=l+1
    else:
        k = (alpha.index(msg[j]) + alpha.index(key[i]))%26
        i = i+1

    ct += alpha[k]
    j = j+1
print(ct)

i=0
j=0
l=0
print('\nDECRYPTION')
while(i<len(key) or j<len(ct)):
    if(i==len(key)):
        k = (alpha.index(msg[j]) - alpha.index(pt[l]))%26
        l=l+1
    else:
        k = (alpha.index(msg[j]) - alpha.index(key[i]))%26
        i = i+1

    pt += alpha[k]
    j = j+1
print(pt)