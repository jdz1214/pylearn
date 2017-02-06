def main():
	execute()


def execute():
	num = max(get_digital_sum(a**b) for a in range(100) for b in range(100))
	print(num)


def get_digital_sum(string) -> int:
	return sum(int(s) for s in str(string))


main()
