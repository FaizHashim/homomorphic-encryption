from random import randint
from sage.all import *

def bytes_to_int(b):
    return int(b.hex(), base=16)

def int_to_bytes(i):
    try:
        t = bytes.fromhex(hex(i)[2:])
    except:
        t = bytes.fromhex('0' + hex(i)[2:])

    return t


class RSA:

    def __init__(self, k, e = 65537):
        while True:
            self.p = randint(2**(k-1), 2**k - 1)
            if is_prime(self.p):
                break
        
        while True:
            self.q = randint(2**(k-1), 2**k - 1)
            if is_prime(self.q):
                break

        self.e = e

        self.n = self.p * self.q

        totient = lcm(self.p - 1, self.q - 1)

        self.d = inverse_mod(self.e, totient)
    def get_public_key(self):
        return (self.n, self.e)

    def encrypt(self, plaintext):
        
        m = bytes_to_int(plaintext)

        if m > self.n:
            raise ValueError
        
        # c= m**self.e % self.n
        c = pow(m, self.e, self.n)
        c = int_to_bytes(c)
        return c

    def decrypt(self, ciphertext):

        c = bytes_to_int(ciphertext)

        if c > self.n:
            raise ValueError

        m = pow(c, self.d, self.n)

        m = int_to_bytes(m)
        return m

