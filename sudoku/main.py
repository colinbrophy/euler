#Program to solve Sudoku Puzzles

import copy
import random

import thepuzzlemodule
thepuzzleo = copy.deepcopy(thepuzzlemodule.thepuzzlemodule1)

thepuzzleg = copy.deepcopy(thepuzzleo) #Keeps original

def startsquare(x):
	startno = 0
	if           x%9 <= 2 and x//9 <=2:
		startno = 0
	if x%9 >=3 and x%9 <= 5 and x//9 <=2:
		startno = 3
	if x%9 >=6 and x%9 <= 8 and x//9 <=2:
		startno = 6

	if x%9 <= 2             and x//9 <=5 and x//9 >= 3:
		startno = 27
	if x%9 <=5 and x%9 >= 3 and x//9 <=5 and x//9 >= 3:
		startno = 30
	if x%9 <=8 and x%9 >= 6 and x//9 <=5 and x//9 >= 3:
		startno = 33

	if x%9 <= 2             and x//9 <=8 and x//9 >=6:
		startno = 54
	if x%9 <=5 and x%9 >= 3 and x//9 <=8 and x//9 >=6:
		startno = 57
	if x%9 <=8 and x%9 >= 6 and x//9 <=8 and x//9 >=6:
		startno = 60
	return startno

def incomplete(puzzle): #Checks if the puzzle guess is finished
	return any(1 != len(i) for i in puzzle)

def duplicates(container):
	container = (i[0] for i in container if len(i) == 1)
	return len(set(container)) != len(list(container))

def incorrect(x): #Check if the puzzle guess is correct
	if any(duplicates(tuple(x[i:9])) for i in range(0, 72, 9)):
		return True
	for b in range(1,10):
#		for n1 in range(0, 74, 9): #Horizontal Line
#			count12 = 0#Reset with each new line being tested
#			for n2 in range(9):
#				if len(x[n1+n2]) == 1 and x[n1+n2] == [b]:
#					count12 += 1
#			if count12 > 1:
#				return True
		for n1 in range(9): #Vertical Line
			count13 = 0
			for n2 in range(0, 74, 9):
				if len(x[n1+n2]) == 1 and x[n1+n2] == [b]:
					count13 += 1
			if count13 > 1:
				return True
		for n1 in range (0, 6 ,3): #9x9 Squares
			for n2 in range(0, 54, 27):
				count14 = 0
				for n3 in range(3):
					for n4 in range(18, 9):
						if len(x[n1+n2+n3+n4]) == 1 and x[n1+n2+n3+n4] == [b]:
							count14 += 1
				if count14 > 1:
					return True
	return False

for n in range(len(thepuzzleo)): #Replace zeros with all poss. values
#			print(repr(thepuzzleo[a][b][c]))
			if thepuzzleo[n] == [0]:
				thepuzzleg[n] = [1,2,3,4,5,6,7,8,9]

guessno = [0]*729             #Generates guessing variable storage
guessbranch = [0,True]
thepuzzlebu = [0]*729

while incomplete(thepuzzleg): #Until it is complete and correct, continue to loop

	thepuzzleoldg = copy.deepcopy(thepuzzleg)

	for n in range(81):
		if len(thepuzzleg[n]) == 1:
			for a in range(3): #9x9 Square
				for b in range(3):
					if len(thepuzzleg[startsquare(n)+b+(9*a)]) != 1:
						if thepuzzleg[n][0] in thepuzzleg[startsquare(n)+b+(9*a)]:
							thepuzzleg[startsquare(n)+b+(9*a)].remove(thepuzzleg[n][0])
			for a in range(9): #Horizontal Line
					if len(thepuzzleg[((n//9)*9)+a]) != 1:
						if thepuzzleg[n][0] in thepuzzleg[((n//9)*9)+a]:
							thepuzzleg[((n//9)*9)+a].remove(thepuzzleg[n][0])
			for a in range(9): #Vertical Line
					if len(thepuzzleg[(n%9)+(a*9)]) != 1:
						if thepuzzleg[n][0] in thepuzzleg[(n%9)+(a*9)]:
							thepuzzleg[(n%9)+(a*9)].remove(thepuzzleg[n][0])

	for a in range(0, 73, 9): #Horizontal Line
		for b in range(1, 10): #Search for each no.
			count1 = 0
			for c in range(9): #Check each item in row
				count1 += thepuzzleg[a+c].count(b)
			if count1 == 1:
				for c in range(9):
					if b in thepuzzleg[a+c]:
						thepuzzleg[a+c] = [b]
						break
	for a in range(9): #Vertical Line
		for b in range(1, 10): #Search for each no.
			count2 = 0
			for c in range(0, 73, 9): #Check each item in line
				count2 += thepuzzleg[a+c].count(b)
			if count2 == 1:
				for c in range(0, 73, 9):
					if b in thepuzzleg[a+c]:
						thepuzzleg[a+c] = [b]
						break
	for a1 in range(0, 6, 3): #9x9 Square
		for a2 in range(0, 55, 27):
			for b in range(1, 10): #Search for each no.
				count3 = 0
				for c in range(9): #Check each item in row
					count3 += thepuzzleg[a1+a2+((c//3)*9)+(c%3)].count(b)
				if count3 == 1:
					for c in range(9):
						if b in thepuzzleg[a1+a2+((c//3)*9)+(c%3)]:
							thepuzzleg[a1+a2+((c//3)*9)+(c%3)] = [b]
							break

	if incorrect(thepuzzleg): #If we made a wrong guess, take a step back
		guessbranch[0] -= 1
		guessbranch[1] = False
		thepuzzleg = copy.deepcopy(thepuzzlebu[guessbranch[0]])
		guessno[guessbranch[0]+1] += 1
		guessno[guessbranch[0]+2] = 0

	if thepuzzleoldg == thepuzzleg or not guessbranch[1]: #If no improvement made or we've gone wrong and are going back

		thepuzzlebu[guessbranch[0]] = copy.deepcopy(thepuzzleg) #Back up the puzzle guess

		guessbranch[0] += 1 #Forming new branch of guesses
		guessbranch[1] = True

		for n1 in range(81): #Find square to guess
			if len(thepuzzleg[n1]) != 1:
				if len(thepuzzleg[n1]) > guessno[guessbranch[0]]:
					thepuzzleg[n1] = [thepuzzleg[n1][guessno[guessbranch[0]]]]
					break
				if len(thepuzzleg[n1]) <= guessno[guessbranch[0]]: #A wrong guess was made earlier
					guessbranch[0] -= 2
					guessbranch[1] = False
					thepuzzleg = copy.deepcopy(thepuzzlebu[guessbranch[0]])
					guessno[guessbranch[0]+1] += 1
					guessno[guessbranch[0]+2] = 0
					break

	#cont = input("Press enter to continue... ")
	#if cont == "1":
	#	break

for a in range(9): #Print finished Sudoku
	if a%3==0:
		print(" ")
	print(repr(thepuzzleg[a*9:(a*9)+9]))
