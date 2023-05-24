

# This file was *autogenerated* from the file exercise-c.sage
from sage.all_cmdline import *   # import sage library

_sage_const_0 = Integer(0); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1)
import sage.all

def Carmichael(N):

    def carmichael(n):

        if n in Primes():
            return False
        
        for i in range(_sage_const_0 , n):
            if i ** n % n != i:
                return False
        return True

    print("The following are the Carmichael numbers below", N, ": ")

    for i in range(_sage_const_2 , N+_sage_const_1 ):
        if carmichael(i):
            print(i)


N = int(input("Enter the value of N : "))
Carmichael(N)
