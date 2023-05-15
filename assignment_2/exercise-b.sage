import random

def return_tuple(k):

    def extended_gcd(p,q):
        if q == 0:
            return 1, 0
        else:
            x, y = extended_gcd(q, p % q)
            return y, x - (p // q) * y

    while True:
        p = random.randint(10**(k-1), 10**k)
        if(p % 2 == 0):
            continue

        if is_prime(p):
            break

    while True:
        q = random.randint(10**(k-1), 10**k)
        if(q % 2 == 0):
            continue

        if is_prime(q) and p != q:
            break

    a, b = extended_gcd(p,q)

    return (p,q,a,b)


k = int(input("Enter the value of k : "))
tup = return_tuple(k)
print("The tuple generated is", tup)