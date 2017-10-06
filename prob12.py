import itertools

def nofactors(no):
	facts = (i for i in range(1, no + 1) if no % i == 0)
	return len(list(facts))

trianglenos = (sum(range(1, i + 1)) for i in itertools.count(1))
for triangleno in trianglenos:
	n = nofactors(triangleno)
	print(triangleno, n)
	if n > 500:
		break
