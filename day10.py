if __name__ == '__main__':
	n = int(input().strip())
	numbers = str(bin(n)[2:]).split('0')


	lenghts = [len(num) for num in numbers]
	print(max(lenghts))




'''
from itertools import groupby
import string 

if __name__ == '__main__':
	n = str(bin(int(input())))
	n = n[2::]

	groups = groupby(n)
	result = [(label, sum(1 for _ in group)) for label, group in groups]
	print(result)
	print(result[0][1])

	

	count = 1

	for i in range(len(n)-1):
		while n[i]==n[i+1]:
			count+=1
		else:
			count=1
	

	print(count)'''

		
		
