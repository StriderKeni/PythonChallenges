if __name__ == '__main__':
	string = []


	for _ in range(int(input())):
		string.append(input())

	for var in string:
		list1 = []
		list2 = []
		for i in range(len(var)):
			if(i%2==0 or i==0):
				list1.append(var[i])
			else:
				list2.append(var[i])
		print("".join(list1) + " " + "".join(list2))

	
	'''for n in range(int(input())):
		list1 = []
		list2 = []
		string = input()


		for i in range(len(string)):
			if (i%2==0 or i==0):
				list1.append(string[i])
			else:
				list2.append(string[i])

		print("".join(list1) + " " + "".join(list2))'''
		



