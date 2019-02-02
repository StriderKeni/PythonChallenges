def split_string(string):
	return '-'.join(string.split(' '))

if __name__ == '__main__':
	line = input()
	result = split_string(line)
	print(result)
