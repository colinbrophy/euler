from functools import lru_cache

def factors(n):
	return set(i for i in range(1, n) if n % i == 0)

@lru_cache(None)
def d(n):
	return sum(factors(n))

amicable = set(i for i in range(1, 10000)
		if d(i) != i and
		i == d(d(i)))

print(sum(amicable))
