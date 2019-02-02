
def is_leap(year):
	
	if year % 400 == 0:
		return True
	if year % 100 == 0:
		return False
	if year % 4 == 0:
		return True
	else:
		return False

    # Write your logic here
	'''if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0):
		leap == True
		return leap'''

if __name__ == '__main__':
	year = int(input())
	print(is_leap(year))

