from math import gcd
from typing import List, Tuple
from helper import *

class RSA:
    BIG_NUMBER: int = 100000000

    def __init__(self, bits: int = 1024, *args, **kwargs) -> None:
        '''
        :param bits: Number of bits to use.
        :param args: Arguments to use as p and q.
            :param p: Prime number.
            :param q: Prime number.
        '''
        def parse_kwargs(p: int = 0, q: int = 0) -> Tuple[int, int]:
            if not (p and q):
                p, q = generate_primes(bits)
            return p, q
        
        p, q = parse_kwargs(**kwargs) 
        self.__p: int = p
        self.__q: int = q
        
        self.n: int = p * q                 # Modulus
        self.__phi: int = (p - 1) * (q - 1) # Euler's totient function
        
        self.e: int = 0                     # Public key
        self.__d: int = 0                   # Private key

        self.e, self.__d = self.generate_keys()
    
    def generate_keys(self) -> Tuple[int, int]:
        e: int = self.e
        d: int = self.__d
        for i in range(2, self.__phi):      # Find e
            if gcd(i, self.__phi) == 1:
                e = i
                break
        for i in range(1, RSA.BIG_NUMBER):  # Find d
            x = 1 + i * self.__phi
            if x % e == 0:                  # type: ignore
                d = int(x / e)
                break
        
        return e, d                         # type: ignore
    
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

