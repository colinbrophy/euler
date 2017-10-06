#!/usr/bin/env python


def ispallindrome(n):
	strn = str(n)
	for i in range(int(len(strn)/2)):
		if strn[i] != strn[-(i+1)]:
			return False
	return True

pallindrome = 0
for x in range(100,1000):
	for y in range(100,1000):
		n = x * y
		if ispallindrome(n) and n > pallindrome: 
			pallindrome = n

print(pallindrome)
