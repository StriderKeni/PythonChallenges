def print_numbers(a,b):
	sum = a + b
	different = a - b
	product = a * b

	return {'sum': sum, 'different': different, 'product': product}

if __name__ == '__main__':
	a = int(input())
	b = int(input())

	dict = print_numbers(a,b)

	print(dict["sum"])
	print(dict["different"])
	print(dict["product"])


