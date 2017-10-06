#!/usr/bin/env python
from math import sqrt
import prime

comp = 600851475143
maxprime = int(sqrt(comp))

for i in range(2,maxprime):
	if comp % i == 0 and prime.isprime(i):
		myprime = i

print(myprime)
