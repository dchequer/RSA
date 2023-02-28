from math import gcd    
from typing import List, Tuple
from helper import *
from random import choice

class RSA:
    '''
    
    
    
    '''
    BIG_NUMBER: int = 100000000
    E_VALUES: List[int] = [3, 5, 17, 257, 65537]

    def __init__(self,bits: int = 1024, *args, **kwargs) -> None:
        '''
        :param bits: Number of bits to use.
        :param args: Arguments to use as p and q.
            :param p: Prime number.
            :param q: Prime number.
        '''
        def parse_kwargs(e: int = 0, p: int = 0, q: int = 0) -> Tuple[int, int, int]:
            if not e:
                e = choice(RSA.E_VALUES)
            if not (p and q):
                p, q = generate_primes(e=e, bits=bits)
            return e, p, q
        
        e, p, q = parse_kwargs(**kwargs)    # int
        self.__p: int = p
        self.__q: int = q
        
        self.n: int = p * q                 # Modulus | part of key | max length of key
        self.__phi: int = (p - 1) * (q - 1) # Euler's totient function
        
        self.e: int = e                     # Public key
        self.__d: int = self.private_key  # Private key
    

    @property
    def __private_key(self) -> int:
        return self.__d
    
    @__private_key.getter
    def private_key(self) -> int:
        '''
        Find appropiate d for current e.
        '''
        return invMod(n=self.__phi, m=self.n)      
    
    def encrypt(self, message: str) -> List[int]:
        '''
        :param message: Message to encrypt.
        '''
        if not message:
            return []

        c: List[int] = []
        for char in message:
            c.append(pow(base=ord(char), exp=self.e, mod=self.n))
        return c

    def decrypt(self, secret: List[int]) -> str:
        '''
        :param secret: Secret to decrypt.
        '''
        if not secret:
            return ''

        m: List[str] = []
        for char in secret:
            temp = pow(base=char, exp=self.__d, mod=self.n)
            print(f'{char} ^ {self.__d} mod {self.n} = {temp}')
            m.append(chr(pow(base=char, exp=self.__d, mod=self.n)))
        return join(m)
    
    @property
    def public_key(self) -> Tuple[int, int]:
        'Returns public key in the form of (e, n)'
        return self.e, self.n
    
    @public_key.setter
    def public_key(self, key: Tuple[int, int]) -> None:
        'Sets public key in the form of (e, n)'
        self.e, self.n = key
    
    def all(self) -> None:
        'Prints all the attributes of the class.'
        print(f'p = {self.__p}')
        print(f'q = {self.__q}')
        print(f'n = {self.n}')
        print(f'phi = {self.__phi}')
        print(f'e = {self.e}')
        print(f'd = {self.__d}')

