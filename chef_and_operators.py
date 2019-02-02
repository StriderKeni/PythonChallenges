
def chef_numbers():


	t = int(input())
	for i in range(t):
		(a,b) = list(map(int,input().split()))
		if(a>b):
			print(">")
		if(a<b):
			print("<")
		if(a==b):
			print("=")

	'''list_numbers = input("List of numbers: ")
	n = list(map(int, list_numbers.split(',')))

	for i in n:

		if(i[n]<i[n+1]):
			print('<')
		elif(i[n]>i[n+1]):
			print('>')
		else:
			print('=')'''


if __name__ == '__main__':
	chef_numbers()