import csv

with open('names.txt', newline='') as f:
	names = sorted(list(csv.reader(f))[0])

def nameval(name):
	return  sum(ord(i) - ord('A') + 1 for i in name)

print(sum((n + 1) * nameval(name) for n, name in enumerate(names)))
