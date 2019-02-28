def count_substring(string, substring):

	ocurrence = sum([1 for i in range(0, len(string)-len(substring)+1) if string[i:i+len(substring)] == substring])

	return ocurrence


if __name__ == '__main__':
	string = input().strip()
	substring = input().strip()
	count = count_substring(string, substring)
	print(count)