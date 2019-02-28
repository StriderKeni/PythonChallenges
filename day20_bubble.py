

if __name__ == '__main__':
	n = int(input().strip())
	arr = list(map(int, input().strip().split(' ')))
	count_swaps = 0

	for i in range(n):

		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				temp = arr[j]
				arr[j] = arr[j+1]
				arr[j+1] = temp
				count_swaps+=1

	print(count_swaps, *arr)

