# Assignment 2

In this assignment, the basics of SageMath was taught along with a bit of number theory. After learning about the topics, the mentee was expected to answer the following exercises:

## Modified Cloud Server:

The cloud server from the previous assignment is modified so that the SageMath module can be introduced into the system in order to perform mathematical operations with much more ease. The `factor()` function in the SageMath module is used in order to calculate the prime factors of the number received from the data owner. This reduces the length of the code considerably due to the presence of the SageMath library.

More details about running the program are present in the README given inside the folder of the exercise.

## SageMath Exercises:

### Exercise A:

The exercise requires to find the first 10 amicable pairs. This is made easy with the help of the divisors function in the SageMath module, with helps us find all divisors of a number. An amicable pair is a pair of numbers in which the sum of the proper divisors of each number is equal to the other number. The code provided calculates the first 10 pairs with ease.

In order to run the program, simply run:
```
sage exercise-a.sage
```

### Exercise B:

In this exercise, a function is to be made that takes in a value `k` and returns a 4-tuple $(p,q,a,b)$ where $p$ and $q$ are distinct k-digit primes and $a$ and $b$ are integers such that $ap + bq = 1$. The k-digit primes are found by randomly picking numbers that have k-digits, and checking if they are prime. Once the two distinct primes are found, we can use the Extended GCD algorithm in order to calculate the values of $a$ and $b$.

In order to run the program, simply run:
```
sage exercise-b.sage
```

### Exercise C:

A Carmichael number is a composite number $n$ that satisfies the following congruence equation:
$$ b^{n}\equiv b{\pmod {n}} $$ for all integers $b$. In this question, we had to create a function that takes in a value $N$ and finds all the Carmichael numbers that are less than or equal to N. This can be done easily with the help of SageMath.

In order to run the program, simply run:
```
sage exercise-c.sage
```
