from collections import deque

d = deque()

for _ in range(int(input())):
	doit = input().split()
	if doit[0]== 'append':
		d.append(doit[1])
	elif doit[0]=='appendleft':
		d.appendleft(doit[1])
	elif doit[0]=='pop':
		d.pop()
	elif doit[0]=='popleft':
		d.popleft()

print(*d)
	


	


