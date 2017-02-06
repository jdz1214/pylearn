def main():
	find_multiple()


def find_multiple():
	num = 1
	found = False
	while not found:
		lst = calculate_equality(num)
		if lst:
			found = compare_multiples(num, lst)
			if found:
				print("Match:")
				print(num)
		num += 1


def calculate_equality(num):
	multiples = []
	for i in range(2, 7):
		m = num * i
		if len(str(m)) == len(str(num)):
			multiples.append(num * i)
		else:
			return False
	return multiples


def compare_multiples(num, multiples):
	numlist = list(str(num))
	numlist.sort()
	for multiple in multiples:
		mlist = list(str(multiple))
		mlist.sort()
		print(''.join(mlist), '::', ''.join(numlist))
		if numlist != mlist:
			return False
	return True


main()
