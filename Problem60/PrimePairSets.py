import itertools

import MathUtils


def main():
	execute()


def execute():
	target = 5
	primestrings = list(map(str, MathUtils.primes_sieve(9999)))
	b = recurve(list(), target, 0, primestrings)
	print(b)


def recurve(lst: list, target: int, pos: int, primestrings: list) -> bool:

	if len(lst) == target:
		print('Found: ')
		print(lst)
		print()
	if pos < len(primestrings):
		for i in range(pos, len(primestrings)):
			n = primestrings[i]
			if check_mutations(lst, n):
				recurve(lst + [n], target, pos + 1, primestrings)


def check_mutations(lst: list, num: str) -> bool:
	if num in lst:
		return False
	if not lst or len(lst) == 1:
		return True
	s = set(map(''.join, itertools.permutations(lst + [num], 2)))
	return all(MathUtils.is_prime(int(p)) for p in s)


# strategy: create combination tuples, then generate permutations for each tuple.

main()
