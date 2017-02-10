import itertools


def main():
	ts = triset()
	ss = squareset()
	ps = pentset()
	hexs = hexset()
	heps = hepset()
	octs = octset()

	groups = [ts, ss, ps, hexs, heps, octs]
	combos = itertools.permutations(groups, len(groups))
	# for c in combos:
	# 	g = list(c)
	# 	for l in g:
	# 		print(l)

	for c in combos:
		recurse(list(), c)


def recurse(lst: list, groups: list):
	n = len(lst)
	if n == len(groups):
		if lst[-1][-2:] == lst[0][:2]:
			print(lst, sum(int(i) for i in lst))

	elif n == 0:
		for i in groups[n]:
			recurse(lst + [i], groups)
	else:
		for i in groups[n]:
			if lst[-1][-2:] == i[:2]:
				recurse(lst + [i], groups)


def triset():
	return list(map(str, list(int(i * (i + 1) / 2) for i in range(45, 141))))


def squareset():
	return list(map(str, list(i**2 for i in range(32, 100))))


def pentset():
	return list(map(str, list(int(i * (3 * i - 1) / 2) for i in range(26, 82))))


def hexset():
	return list(map(str, list(i * (2 * i - 1) for i in range(23, 71))))


def hepset():
	return list(map(str, list(int(i * (5 * i - 3) / 2) for i in range(21, 64))))


def octset():
	return list(map(str, list(i * (3 * i - 2) for i in range(19, 59))))


main()
