import itertools


def num_permute(num):
	l = []
	__num_permute(l, '', num)
	return l


def __num_permute(l, prefix, numdigits) -> None:
	if len(prefix) == numdigits:
		l.append(prefix)
	else:
		for j in range(0, 10):
			__num_permute(l, prefix + str(j), numdigits)


def permute(string) -> set:
	perms = [''.join(p) for p in itertools.permutations(string)]
	return set(perms)


def is_palindrome(string) -> bool:
	s = str(string)
	rev = s[::-1]
	return rev == s


def get_palindrome(string) -> str:
	return str(string)[::-1]
