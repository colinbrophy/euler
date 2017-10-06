import functools
from math import floor, sqrt
from collections import Counter

maxno = 64000000
factor = lambda n ,factor: n % factor == 0

@functools.lru_cache(maxsize=None)
def sumgeoseries(a, n):
	"""sum of r= 0 to n a^(2r)"""
	return sum(a**(2*r) for r in range(n + 1))
#	return (a**(2*n + 2) - 1) // (a*a - 1)

perfect_squares = set(i*i for i in range(1, floor(sqrt(maxno))))

@functools.lru_cache(maxsize=None)
def sumsqdiv(n):
	for i in range(2, floor(sqrt(n)) + 1):
		power = 0
		while factor(n ,i):
			power += 1
			n //= i
		if power != 0:
			return sumgeoseries(i, power) * sumsqdiv(n)
	return n*n + 1 # Must be prime if reached

print(1 + sum(i for i in range(2, maxno)
	if sumsqdiv(i) in perfect_squares))
#	if sqrt(sumsqdiv(i)).is_integer()))
