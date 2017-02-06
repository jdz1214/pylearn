import Utils.TextUtils
import Utils.MathUtils


def main():
	familysize = 7
	find_family(familysize)


def find_family(familysize):
	primefamily = prime_digit_replacements(familysize)
	if primefamily:
		print("Found ", len(primefamily), " prime families of size ", familysize, ":")
		counter = 1
		for p in primefamily:
			print("Family ", counter, ":")
			for f in p:
				print(f)
			print()
			counter += 1
	else:
		print("Did not find prime family.")


def prime_digit_replacements(familysize):
	for i in range(2, 7):
		combos = set()
		families = []
		for j in range(1, i):
			digits = Utils.TextUtils.num_permute(i - j)
			for d in digits:
				s = (Utils.TextUtils.permute('*' * j + d))
				for val in s:
					combos.add(val)
		for combo in combos:
			primelist = check_combo(combo)
			if len(primelist) == familysize:
				families.append(primelist)
		if len(families) > 0:
			return families


def check_combo(combo):
	primelist = []
	for i in range(0, 10):
		x = combo
		newx = ''
		for letter in x:
			if letter == '*':
				newx += str(i)
			else:
				newx += letter
		num = int(newx)
		if len(str(num)) == len(combo) and Utils.MathUtils.is_prime(num):
			primelist.append(num)
	return primelist

main()
