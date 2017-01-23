import math


def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False
	return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def gen_primes(lowerinclusive, upperexclusive):
	primes = []

	if lowerinclusive <= 2 < upperexclusive:
		primes.append(2)
		if upperexclusive > 3:
			lowerinclusive = 3
		else:
			return primes

	for i in range(lowerinclusive, upperexclusive):
		if is_prime(i):
			primes.append(i)

	return primes