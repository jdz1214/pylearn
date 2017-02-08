import math


def is_prime(n):
	if n < 2:
		return False
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


def primes_sieve(upperinclusive):  # sieve of eratosthenes
	ps, sieve = [], [True] * (upperinclusive + 1)
	for p in range(2, upperinclusive + 1):
		if sieve[p]:
			ps.append(p)
			for i in range(p * p, upperinclusive + 1, p):
				sieve[i] = False
	return set(ps)


def get_factorial(num):
	if num == 0 or num == 1:
		return 1
	if num == 2:
		return 2
	factorial = num
	while num > 2:
		num -= 1
		factorial *= num
	return factorial
