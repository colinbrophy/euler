import math

def fib_next_value(a, b):
	return fib_next_value(b, a + b)

def isprime(n):
	maxfact = math.floor(math.sqrt(n))
	for i in range(2, maxfact):
		if n % i == 0:
			return False
	return True

def sumdigits(n):
	return sum(int(i) for i in str(n))

def prop_divisors(n):
	maxdiv = math.floor(math.sqrt(n))
	yield 1
	for i in range(2, maxdiv + 1):
		if n % i == 0:
			yield i
			if int(n / i) != i:
				yield int(n / i)
