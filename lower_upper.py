'''if __name__ == '__main__':
	string = input()
	new_string = []

	for char in string:
		try: 
			if char.islower():
				new_string.append(char.upper())
			else:
				new_string.append(char.lower())
		except:
			new_string.append(char)


	print(''.join(new_string))'''



def swap_case(string):
	new_string = []
	for char in string:
		if char.islower():
			new_string.append(char.upper())
		else:
			new_string.append(char.lower())

	return (''.join(new_string))



if __name__ == '__main__':
	s = input()
	result = swap_case(s)
	print(result) 
