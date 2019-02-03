from itertools import groupby

if __name__ == '__main__':
	s = input()
	group_list = []

	for k, c in groupby(s):
		group_list.append((len(list(c)), int(k)))

	print(*group_list)

	





