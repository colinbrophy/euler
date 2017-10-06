#!/usr/bin/env python

import prime

primen = 0
n = 2 
while primen < 10001:
	if prime.isprime(n):
		primen += 1
		myprime = n
	n += 1

print(myprime)
