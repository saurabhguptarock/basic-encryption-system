result = ''
print('You want to Encrypt or Decrypt the message \n 1. Encrypt\n 2. Decrypt')
choice = input()
if choice == '1':
    print('Enter Message to be encrypted')
    z = input()
    for i in range(0, len(z)):
        result = result + chr(ord(z[i]) + 7)

    print(result + '\n\n')
    result = ''

elif choice == '2':
    print('Enter Mesage to be decrypted')
    z = input()
    for i in range(0, len(z)):
        result = result + chr(ord(z[i]) - 7)

    print(result + '\n\n')
    result = '1'

else:
    print('Wrong Choice')
