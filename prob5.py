#!/usr/bin/env python

n = 20

found = False
while not found:
	n += 1
	found = True # Assume you have found it until it fails
	for i in range(2, 20):
		if n % i != 0:
			found = False
			break
print(n)
