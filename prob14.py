def generateseq(start):
	n = start
	while n > 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3 * n + 1
		yield n
	yield n

maxseqlenstart = max(range(1, 1000000), key=lambda x: len(list(generateseq(x))))

print(maxseqlenstart)
