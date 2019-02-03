import datetime

def time_delta(t1,t2):
	diff = t1 - t2
	return int(abs(diff.total_seconds()))

if __name__ == '__main__':
	t1 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
	t2 = datetime.datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
	
	#t2 = input().rstrip().split()
	delta = time_delta(t1,t2)
	print(delta)
