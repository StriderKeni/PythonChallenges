if __name__ == '__main__':

	string = input().strip()
	numeric = False
	alpha = False
	digit = False
	lower = False
	upper = False

	for char in string:
		print(char)
		if str(char).isalnum():
			numeric = True
		if str(char).isalpha():		
			alpha=True
		if str(char).isdigit():
			digit=True
		if str(char).islower():
			lower=True		
		if str(char).isupper():
			upper=True


	print(numeric)
	print(alpha)
	print(digit)
	print(lower)
	print(upper)


	
