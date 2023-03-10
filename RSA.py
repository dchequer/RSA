from math import gcd    
from typing import List, Tuple
from helper import *
from random import choice

class RSA:
    '''
    RSA encryption algorithm.
    Accepts values for e, p, q, and d. Alternatively, it will generate them.
    Can be given a number of bits to use. If not, it will use 1024.
    
    Examples
    --------
    ```
    from RSA import RSA

    rsa1 = RSA(bits = 16)                                                   # generate e, p, q.  
    rsa2 = RSA(bits = 64, e = 5, p = 38839, q = 14563, d = 412737137)       # use given values.  
    rsa3 = RSA(bits = 32, e = 7, p = 38839, q = 14563)                      # generate d.  
    rsa4 = RSA(bits = 128, e = 65537)                                       # generate p, q, d.  
    ```

    
    '''
    #BIG_NUMBER: int = 100000000
    E_VALUES: List[int] = [3, 5, 17, 257, 65537]

    def __init__(self,bits: int = 1024, **kwargs) -> None:
        '''
        :param bits: Number of bits to use.
        :param kwargs: Keyword arguments to use as e, p, and q.
            :param e: Public key exponent.
            :param p: Prime number.
            :param q: Prime number.
            :param d: Private key exponent.
        '''
        def parse_kwargs(e: int = 0, p: int = 0, q: int = 0, d: int = 0) -> Tuple[int, int, int, int]:
            if not e:
                e = choice(RSA.E_VALUES)
            if not (p and q):
                p, q = generate_primes(e=e, bits=bits)
            if not d:
                d = self.private_key
            return e, p, q, d
        
        e, p, q, d = parse_kwargs(**kwargs)    # int
        self.__p: int = p
        self.__q: int = q
        
        self.n: int = p * q                 # Modulus | part of key
        self.__phi: int = (p - 1) * (q - 1) # Euler's totient function
        
        self.e: int = e                     # Public key
        self.__d: int = d                   # Private key
    

    @property
    def __private_key(self) -> int:
        return self.__d
    
    @__private_key.getter
    def private_key(self) -> int:
        '''
        Find appropiate d for current e.
        '''
        return invMod(self.e, self.__phi)      
    
    def encrypt(self, message: str) -> List[int]:
        '''
        :param message: Message to encrypt.
        '''
        if not message:
            return []

        c: List[int] = []
        for char in message:
            c.append(pow(base=ord(char), exp=self.e, mod=self.n))       # c = m^e mod n
        return c

    def decrypt(self, secret: List[int]) -> str:
        '''
        :param secret: Secret to decrypt.
        '''
        if not secret:
            return ''

        m: List[str] = []
        for char in secret:
            m.append(chr(pow(base=char, exp=self.__d, mod=self.n)))    # m = c^d mod n
        return join(m)
    
    @property
    def public_key(self) -> Tuple[int, int]:
        '''Returns public key in the form of (e, n)'''
        return self.e, self.n
    
    @public_key.setter
    def public_key(self, key: Tuple[int, int]) -> None:
        '''Sets public key in the form of (e, n)'''
        self.e, self.n = key
    
    def all(self) -> None:
        '''Prints all the attributes of the class.'''
        print(f'p = {self.__p}')
        print(f'q = {self.__q}')
        print(f'n = {self.n}')
        print(f'phi = {self.__phi}')
        print(f'e = {self.e}')
        print(f'd = {self.__d}')

