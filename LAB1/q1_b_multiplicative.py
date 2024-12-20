alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
msg = input('Enter the message to be encrypted : ')
key = int(input('Enter the key : '))
j=0
ct = ''
pt = ''
print('MULTIPLICATIVE CIPHER')
print('ENCRYPTION \n' )
for i in msg:
    j = alpha.index(i)
    ct += alpha[(j*key)%26]
print(ct)

print('\nDECRYPTION \n')
for i in ct:
    j = alpha.index(i)
    pt += alpha[(j*pow(key,-1,26))%26]
print(pt)