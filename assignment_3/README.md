# Assignment 3

In this assignment, we will be implemented different types of cryptosystems, namely - the RSA cryptosystem, the ElGamal cryptosystem and the Paillier cryptosystem.

## RSA Cryptosystem

In the file `RSA.py`, we have implemented an RSA class. This class takes in the value of $k$ in the constructor, and generates two k-bit primes. The constructor also has an optional parameter for $e$, which is set to 65567 by default.

In order to initialize the object, first import the file:
```
import RSA
```
After importing, you can use the class by calling
```
my_rsa = RSA.RSA(k = 10)
```

## ElGamal Cryptosystem

In the file `ElGamal.py`, the ElGamal class has been implemented. The class takes in the value of $g$ and $p$ in its constructor.

In order to initialize the object, first import the file:
```
import ElGamal
```
After importing, you can use the class by calling
```
my_eg = ElGamal.ElGamal(g, p)
```

## Paillier Cryptosystem

In the file `Paillier.py`, the Paillier class is implemented. The class takes in the value of $k$ in the constructor, and generates two k-bit primes.

In order to initialize the object, first import the file:
```
import Paillier
```
After importing, you can use the class by calling
```
my_pai = Paillier.Paillier(k = 10)
```