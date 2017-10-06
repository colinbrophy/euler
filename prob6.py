#!/usr/bin/env python

def sumsquares(n):
	ret = 0 
	for i in range(1,n+1):
		ret += i ** 2
	return ret

def squaressum(n):
	sum = 0.5 * n * (n+1) # Use sum of n formula
	return sum ** 2

n = int(squaressum(100) - sumsquares(100))

print(n)
