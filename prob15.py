total = 0
def walk_grid(x, y):
	global total
	if x == 20 and y == 20:
		total += 1
	else:
		if x != 20:
			walk_grid(x + 1, y)
		if y != 20:
			walk_grid(x, y + 1)

walk_grid(1, 1)
print(total)
