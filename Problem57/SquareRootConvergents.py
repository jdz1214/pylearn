def main():
	print(step(1000))


def step(steps):
	print('Step:  1  ', '3 / 2')
	count = 0
	numerator = 3
	denominator = 2
	for i in range(2, steps + 1):
		old_denominator = denominator
		denominator += numerator
		numerator = denominator + old_denominator
		if len(str(numerator)) > len(str(denominator)):
			count += 1
		print('Step: ', i, ' ', numerator, '/', denominator)
	return count

	# the new denominator is the sum of the old denominator and the old numerator.
	# the new numerator is the sum of the new denominator and the old denominator.

main()
