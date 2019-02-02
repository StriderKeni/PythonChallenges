if __name__ == '__main__':

	list = []

	for _ in range(int(input())):
		instr = input().split()
		if instr[0] == 'insert':
			list.insert(int(instr[1]), int(instr[2]))
		elif instr[0] == 'print':
			print(list)
		elif instr[0] == 'remove':
			list.remove(int(instr[1]))
		elif instr[0] == 'append':
			list.append(int(instr[1]))
		elif instr[0] == 'sort':
			list.sort()
		elif instr[0] == 'reverse':
			list.reverse()
		elif instr[0] == 'pop':
			list.pop()




