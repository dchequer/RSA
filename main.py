from RSA import RSA
from helper import *


if __name__ == '__main__':
    rsa = RSA(bits = 16)
    og = 'hello world'
    enc_og = rsa.encrypt(og)
    dec_og = rsa.decrypt(enc_og)
    print(f'Original: {og}')
    print(f'Encrypted: {join(enc_og)}')
    print(f'Decrypted: {dec_og}')
