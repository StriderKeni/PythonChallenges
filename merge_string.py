import textwrap
from collections import OrderedDict 

def merge_the_tools(string, k):

	str1 = textwrap.wrap(string, k)
	str2 = []

	for i in str1:
		str2.append("".join(OrderedDict.fromkeys(i)))

	for y in str2:
		print(y)

if __name__ == '__main__':
	string, k = input(), int(input())
	merge_the_tools(string, k)














'''
if __name__ == '__main__':
	str1 = input()
	k = int(input())

	n = int(len(str1)/k)

	for x in range(0, len(str1), n):
		print(''.join(set(str1[x:(x+3)])))
'''




