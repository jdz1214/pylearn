import TextUtils


def main():
	execute()


def execute():
	lychrelcount = [is_lychrel(i) for i in range(10000)].count(True)
	print('Lychrels below 10,000: ', lychrelcount)


def is_lychrel(num) -> bool:
	for i in range(0, 50):
		num = pal_iteration(num)
		if TextUtils.is_palindrome(num):
			return False
	return True


def pal_iteration(num) -> int:
	rev = int(TextUtils.get_palindrome(num))
	return num + rev

main()
