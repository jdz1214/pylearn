import regex as regex

import Utils.MathUtils


def main():
	prime_digit_replacements(8)


def prime_digit_replacements(digits):
	# goal: print out matches.
	# replace every occurence of each digit 1-9 in sets and see what patterns arise
	primesfive = Utils.MathUtils.gen_primes(10000, 99999)

	primestring = ""

	for prime in primesfive:
		primestring += str(prime) + "\n"

	for first in range(0, 10):
		for second in range(0, 10):
			for third in range(0, 10):
				zee = str(first) + str(second) + "((\d)\\2)" + str(third)
				p = regex.compile(zee)
				replacedstrings = regex.finditer(p, primestring)

				relist = list(replacedstrings)
				if len(relist) == 7:
					for l in relist:
						print(l.group(0))


main()
