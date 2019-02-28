def square_numbers(nums):
	for i in nums:
		yield (i*i)


if __name__ == '__main__':
	
	list_nums = [1,2,3,4,5,6,7,8]

	my_nums = square_numbers(list_nums)

	for num in my_nums:
		print(num)


'''
def square_numbers(nums):
	result = []
	for i in nums:
		result.append(i*i)

	return result


if __name__ == '__main__':
	
	list_nums = [1,2,3,4,5,6,7,8]
	my_square = square_numbers(list_nums)
	print(*my_square)
'''