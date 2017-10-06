import itertools
from utils import prop_divisors

maxabundant = 28123
abundant = set(i for i in range(1, maxabundant + 1) if sum(prop_divisors(i)) > i)
print(abundant)
notsumabundant = sum(i for i in range(1, maxabundant + 1) if not any((i - a in
	abundant) for a in abundant))

print(notsumabundant)
