import itertools
import string


def main():
	load()


def load():
	with open('p059_cipher.txt', 'r') as f:
		lines = f.readlines()
	f.close()
	s = lines[0]
	digitlist = s.split(',')
	execute(digitlist)


def execute(digitlist):
	xors = list(perm(3, string.ascii_lowercase))
	translations = []
	cipher = ''
	for digit in digitlist:
		cipher += chr(int(digit))
	for xor in xors:
		decoded = sxor(cipher, xor * 1000)
		valsum = str(sum(ord(x) for x in decoded))
		record = 'xor: ' + xor + ' ascii sum: ' + valsum + '\n' + decoded
		translations.append(record)

	# print('Translations: ')
	for t in translations:
		if 'The Gospel of John' in t:
			print(t)


def perm(n, seq):
	lst = []
	for p in itertools.product(seq, repeat=n):
		lst.append("".join(p))
	return lst


def sxor(s1, s2):
	# convert strings to a list of character pair tuples
	# go through each tuple, converting them to ASCII code (ord)
	# perform exclusive or on the ASCII code
	# then convert the result back to ASCII (chr)
	# merge the resulting array of characters as a string
	return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

main()
