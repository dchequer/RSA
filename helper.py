from typing import List, Any, Tuple
from random import getrandbits

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

def isPrime(n: int) -> bool:
    '''
    Check if a number is prime.
    :param n: Number to check.
    '''
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_primes(bits: int = 1024) -> Tuple[int, int]:
    '''
    Generate two prime numbers.
    :param bits: Number of bits to use.
    '''
    p: int = 0
    q: int = 0
    while not isPrime(p):
        p = getrandbits(bits)
    while not isPrime(q):
        q = getrandbits(bits)
    return p, q

if __name__ == '__main__':
    print(generate_primes(bits=8))