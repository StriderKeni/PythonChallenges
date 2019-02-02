if __name__ == '__main__':
	
	phonesBook = {}
	n = int(input())

	for _ in range(n):
		name, num = input().strip().split()
		phonesBook[name] = num

	while (True):
		try:
			qName = input().strip()
			if qName in phonesBook:
				print("{}={}".format(qName, phonesBook[qName]))
			else:
				print("Not found")
		except EOFError:
			break

