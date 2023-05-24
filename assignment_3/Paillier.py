from sage.all import is_prime, lcm, gcd, inverse_mod, mod
from random import randint


def bytes_to_int(b):
    return int(b.hex(), base=16)

def int_to_bytes(i):
    # print(hex(i)[2:])
    try:
        t = bytes.fromhex(hex(i)[2:])
    except:
        t = bytes.fromhex('0' + hex(i)[2:])

    return t

def mod_exp(b, e, m):
    c = (b % m)
    e1 = 1
    while (e1 < e):
        c = (c * b) % m
        e1 = e1 + 1

    return c

class Paillier:

    def __init__(self, k) -> None:
        while True:
            try:
                while True:
                    while True:
                        self.p = randint(2**(k-1), 2**k - 1)
                        if is_prime(self.p):
                            break
                    
                    while True:
                        self.q = randint(2**(k-1), 2**k - 1)
                        if is_prime(self.q):
                            break

                    if gcd(self.p*self.q, (self.p-1)*(self.q-1)) == 1:
                        break

                # print(self.p, self.q)

                        
                self.n = self.p * self.q

                

                L = lambda x: (x - 1) / self.n

                self.lamd = lcm(self.p-1, self.q-1)
                
                # print(self.lamd)

                self.g = randint(1, self.n ** 2)

                # print(self.g)

                self.mu = inverse_mod(L( mod_exp(self.g, self.lamd, (self.n**2) )) , self.n)
                
                # print(self.mu)
                break
            except ZeroDivisionError:
                # print("truing")
                continue

    def get_public_key(self):
        return (self.n, self.g)

    def encrypt(self, plaintext):
        # m = bytes_to_int(plaintext)
        m = plaintext

        if m >= self.n:
            print("Error")
            raise ValueError        

        r = randint(1, self.n - 1)
        # print('r:',r)
        # print('n:',self.n)

        # c = (self.g ** m * r ** self.n) % self.n ** 2
        c = mod_exp(self.g, m, self.n**2) * mod_exp(r, self.n, self.n**2)  % self.n**2
        # c = int_to_bytes(c)
        return c


    def decrypt(self, ciphertext):
        
        c = ciphertext
        # c = bytes_to_int(ciphertext)
        
        L = lambda x: (x - 1) / self.n
        
        m = int(( L(mod_exp(c, self.lamd, self.n**2)) * self.mu ) % self.n)
    
        # m = int_to_bytes(int(m))
        return m