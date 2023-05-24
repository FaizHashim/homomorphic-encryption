from random import randint
from sage.all import *

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
            


        self.p = 61
        self.q = 53

        self.e = e

        self.n = self.p * self.q

        totient = lcm(self.p - 1, self.q - 1)
        
        self.d = inverse_mod(self.e, totient)



    def get_public_key(self):
        return (self.n, self.e)

    def encrypt(self, plaintext):
        m = int(plaintext.hex(), base=16)
        m = 65
        if m > self.n:
            raise ValueError

        c = mod(m, self.n)
        e1 = 1
        while (e1 < self.e):
            c = mod(c * m, self.n)
            e1 += 1

        # c= m**self.e % self.n

        return c

    def decrypt(self, ciphertext):
        print(ciphertext, self.d, self.n)
        return (ciphertext^self.d), self.n 


x = RSA(40, 17)
# print(x.p)
# print(x.q)
# print(x.e)
print(x.encrypt(b'hi'))
print(x.decrypt(2790))