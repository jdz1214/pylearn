import itertools


def num_permute(num):
	l = []
	__num_permute(l, '', num)
	return l


def __num_permute(l, prefix, numdigits):
	if len(prefix) == numdigits:
		l.append(prefix)
	else:
		for j in range(0, 10):
			__num_permute(l, prefix + str(j), numdigits)


def permute(string):
	perms = [''.join(p) for p in itertools.permutations(string)]
	return set(perms)