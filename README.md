# RSA
RSA encryption and decryption
Simple RSA Encryption algorithm 

### Facts about RSA encryption and usage

***

- RSA encryption is purely mathemical, therefore all inputs must be numerical.  
  - Convert any inputs like text to numbers using things conventions like ASCII or Unicode.  
- n is the maximum length for encryption/decryption, it is also called modulus or key length
  - Make sure that you are using values that are not too big for your chosen n
  - You can do the following to increase your n:
    - Manually choose larger p and q
    - Use more bits (1024 is usually the minimum)
- Generating large primes and private keys can be time (and resource) comsuming, however this is unimportant as keys are not calculated in real-time frequently
  - They should usually be updated regularly depending on application, but monthly is a good starting point
