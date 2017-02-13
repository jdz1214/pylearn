import itertools


def main():
	cubelist = set(map(str, set(i**3 for i in range(1, 2000))))
	finished = False
	for i in range(1282, 2000):
		print(i)
		if finished:
			break
		found = []
		pcount = 0
		permutations = set(map(''.join, itertools.permutations(str(i**3))))
		for p in permutations:
			if p in cubelist:
				pcount += 1
				found.append(i**3)
		if pcount == 5:
			print('Solution found. i: ', i, ' cube: ', i**3,)
			print(found)
			finished = True


main()
