from typing import List, Any, Tuple
from random import getrandbits
from math import gcd
from time import time

def timer_func(func):
    '''This function shows the execution time of 
    the function object passed'''
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func

def join(*args, **kwargs) -> str:
    '''
    Join a list of items into a string.
    :param lst: List of items to join.
    :param args: Arguments to pass to the join function.
        sep: Separator to use between items.
        end: String to append to the end of the string.
    '''

    # If no arguments are passed, return an empty string.
    if not args:
        return ''

    def parse_kwargs(sep: str = '', end: str = '') -> Tuple[str, str]:
        return sep, end
    
    sep, end = parse_kwargs(**kwargs)       # str
    lst: List[Any] = args[0]                # List[any]
    output: str = str(lst[0])
    for item in lst[1:]:
        output += sep + str(item)
    output += end

    return output

#@timer_func
def isPrime(n: int, **kwargs) -> bool:
    '''
    Check if a number is prime.
    :param n: Number to check.
    :param kwargs: Keyword arguments to pass to the function.
        :param k: Optional co-prime | only common factor is 1.
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    def parse_kwargs(k: int = 0) -> int:
        return k
    
    if (kwargs := parse_kwargs(**kwargs)) != 0:     # find if co-prime
        return gcd(n, kwargs) == 1
                 
    i = 5                                           # start at 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0: 
            return False                            # a common factor has been found
        i += 6
    return True                                     # no common factors

def newPrime(bits: int) -> int:
    '''
    Generate a new prime number.
    :param bits: Number of bits to use.
    '''
    return getrandbits(bits) | 1 # make sure it's odd

#@timer_func
def generate_primes(e: int, bits: int = 1024) -> Tuple[int, int]:
    '''
    Generate two prime numbers (p, q), given a public key exponent.
    p * q must not exceed bits in length.
    :param e: Public key exponent.
    :param bits: Number of bits to use.
    '''
    p: int = 0
    q: int = 0
    while not isPrime(n=p, k=e):
        #print('finding p')
        p = newPrime(bits=bits//2)
    while not isPrime(q, k=e):
        #print('finding q')
        q = newPrime(bits=bits - bits//2)
    #print('done!')
    #print(p, q)
    return p, q

def invMod(n: int, m: int) -> int:
    '''
    Find the multiplicative inverse of n mod m.
    :param n: Number to find the inverse of.
    :param m: Modulus.
    '''
    for i in range(1, m):
        if (n * i) % m == 1:
            return i
    return 1
    

if __name__ == '__main__':
    #print(generate_primes(e=257, bits=128))
    #write tests and time the isPrime function:
    #print(isPrime(257_000_123_751_953_728_929_012_131_872_999_999_999_222))
    prime1, prime2 = generate_primes(e=3, bits=64)
    #prime1 = 6_566_426_039_484_363_671      # 6566426039484363671
    #prime2 = 6_369_492_118_272_615_259      # 6369492118272615259

    print(f'{prime1:,} {prime2:,}')
    print(isPrime(n=prime1, k=3), isPrime(n=prime2, k=3))
