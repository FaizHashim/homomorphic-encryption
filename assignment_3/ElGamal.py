from sage.all import *
import random

def bytes_to_int(b):
    return int(b.hex(), base=16)

def int_to_bytes(i):
    try:
        t = bytes.fromhex(hex(i)[2:])
    except:
        t = bytes.fromhex('0' + hex(i)[2:])

    return t


class ElGamal:

    def __init__(self, g, p) -> None:
        self.g = g
        self.p = p
        
        self.b = random.randint(1, self.p - 1)
        
        # self.h = (self.g**self.b) % self.p
        self.h = pow(self.g, self.b, self.p)


    def get_public_key(self):
        return (self.p, self.g, self.h)

    def encrypt(self, plaintext):
        
        m = bytes_to_int(plaintext)

        if m >= self.p:
            print("Error")
            raise ValueError
        
        a = random.randint(1, self.p - 1)
        
        # s = (self.h ** a)  % self.p
        s = pow(self.h, a, self.p)
        
        # c1 = (self.g ** a) % self.p
        c1 = pow(self.g, a, self.p)
        c2 = (m * s) % self.p

        c1 = int_to_bytes(c1)
        c2 = int_to_bytes(c2)
        return (c1, c2)

    def decrypt(self, ciphertext):
        
        c1 = bytes_to_int(ciphertext[0])
        c2 = bytes_to_int(ciphertext[1])

        # s = (c1 ** self.b) % self.p
        s = pow(c1, self.b, self.p)

        s_inv = inverse_mod(s, self.p)

        m = (c2 * s_inv) % self.p
        return int_to_bytes(m)

x = ElGamal(2, 19813)
print(x.get_public_key())
y = (x.encrypt(b'a'))
print(y)
print(x.decrypt(y))



