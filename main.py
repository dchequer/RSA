from RSA import RSA
from helper import *


if __name__ == '__main__':
    preset = { 
        'e': 65537,
        'p': 38839,
        'q': 14563,
        'd': 412737137
    }

    rsa = RSA(bits = 32, **preset)
    rsa.all()
    '''
    og = 'hello world'
    print(f'Original: {og}')
    print(f'Original: {[ord(ch) for ch in og]}')
    enc_og = rsa.encrypt(og)
    print(f'Encrypted: {(enc_og)}')
    dec_og = rsa.decrypt(enc_og)
    print(f'Decrypted: {dec_og}')
    '''

    still = True
    msg = ''
    while still:
        print('1. New Message')  
        print('2. Exit')
        choice = int(input('Enter choice: '))
        match choice:
            case 1:
                msg = input('Enter message: ')
                enc = rsa.encrypt(msg)
                dec = rsa.decrypt(enc)
                print(f'Original: {msg}')
                print(f'Encrypted: {enc}')
                print(f'Decrypted: {dec}')
            case 2:
                still = False
            case _:
                print('Invalid choice')


