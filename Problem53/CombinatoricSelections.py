import Utils.MathUtils


def main():
	combinatorics()


def combinatorics():
	millioncount = 0
	for n in range(1, 101):
		for r in range(1, n + 1):
			ncr = get_ncr(n, r)
			if ncr >= 1000000:
				millioncount += 1
	print(millioncount)


def get_ncr(n, r):
	ncr = 0
	if r <= n:
		diff = n - r
		nfact = Utils.MathUtils.get_factorial(n)
		rfact = Utils.MathUtils.get_factorial(r)
		dfact = Utils.MathUtils.get_factorial(diff)

		ncr = nfact / (rfact * dfact)
	return ncr


main()
