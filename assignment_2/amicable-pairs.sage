from sage.all import *

amicable = []
count = 0

x = 2

while count < 10:
    y = sum(divisors(x)[:-1])
    if (sum(divisors(y)[:-1]) == x) and (x != y) and ( (y,x) not in amicable):
        amicable.append((x,y))
        count += 1
    x += 1

print("Here are 10 distinct amicable pairs:")

for i, pair in enumerate(amicable,1):
    print(i,"\b.", pair)