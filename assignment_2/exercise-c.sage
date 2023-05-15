import sage.all

def Carmichael(N):

    def carmichael(n):

        if n in Primes():
            return False
        
        for i in range(0, n):
            if i ^ n % n != i:
                return False
        return True

    print("The following are the Carmichael numbers below", N, ": ")

    for i in range(2, N+1):
        if carmichael(i):
            print(i)


N = int(input("Enter the value of N : "))
Carmichael(N)