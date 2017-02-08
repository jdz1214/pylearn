import MathUtils


def main():
	spiral_primes()


def spiral_primes():
	count = 1
	loop = 1
	allcount = 1
	primecount = 0

	while True:
		sidelength = loop * 2
		for i in range(1, 5):
			# print('i ', i)
			count += sidelength
			if MathUtils.is_prime(count):
				primecount += 1
		allcount += 4
		ratio = primecount / allcount
		if ratio < 0.1:
			print('primecount ', primecount, ' allcount ', allcount, ' ratio ', ratio, ' sidelength ', sidelength + 1)
			break

		loop += 1


main()
