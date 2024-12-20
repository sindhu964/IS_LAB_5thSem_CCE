alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = input('Enter the message to be encrypted : ')
key1 = int(input('Enter the key : '))
key2 = int(input('Enter the key : '))
j=0
ct = ''
pt = ''

print('ENCRYPTION \n' )
for i in msg:
    if(i == ' '):
        ct += ' '
    else:
        j = alpha.index(i)
        ct += alpha[((j*key1)+key2)%26]
print(ct)

print('\nDECRYPTION \n')
for i in ct:
    if(i== ' '):
        pt += ' '
    else:
        j = alpha.index(i)
        pt += alpha[((j-key2)*pow(key1,-1,26))%26]

print(pt)