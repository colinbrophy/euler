import math

def isprime(n):
	maxfact = int(math.sqrt(n)) + 1
	for i in range(2, maxfact):
		if n % i == 0:
			return False
	return True

