def find_missing(arr1, arr2):
	missings = []

	for i in range(len(arr1)):
		if arr1[i] not in arr2:
			missings.append(arr1[i])
		else:
			continue
			
	return missings

if __name__ == '__main__':
	arr1 = [4,12,9,5,6,78,45,15,13]
	arr2 = [4,9,12,6]

	print(find_missing(arr1, arr2))