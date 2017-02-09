def main():
	ts = triset()
	ss = squareset()
	ps = pentset()
	hexs = hexset()
	heps = hepset()
	octs = octset()


def triset():
	return set(int(i * (i + 1) / 2) for i in range(45, 141))


def squareset():
	return set(i**2 for i in range(32, 100))


def pentset():
	return set(int(i * (3 * i - 1) / 2) for i in range(26, 82))


def hexset():
	return set(i * (2 * i - 1) for i in range(23, 71))


def hepset():
	return set(int(i * (5 * i - 3) / 2) for i in range(21, 64))


def octset():
	return set(i * (3 * i - 2) for i in range(19, 59))


main()
