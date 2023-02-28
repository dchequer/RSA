from RSA import RSA
from helper import *


if __name__ == '__main__':
    rsa = RSA(bits = 32, e = 257)
    rsa.all()
    og = 'hello world'
    print(f'Original: {og}')
    print(f'Original: {[ord(char) for char in og]}')
    enc_og = rsa.encrypt(og)
    print(f'Encrypted: {(enc_og)}')
    dec_og = rsa.decrypt(enc_og)
    print(f'Decrypted: {dec_og}')


