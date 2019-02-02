def value_dict(key, dict):
	for k, v in dict.items():
		if key == k:
			return (k+"="+v)

if __name__ == '__main__':
	arr = []
	names = []
	phone_name = []
	total = int(input())
	
	for _ in range(total):
		arr.append(tuple(input().split(" ")))

	dict_phones = dict((x, y) for x,y in arr)

	for _ in range(total):
		names.append(input())

	for k in names:
		phone_name.append("Not found" if (value_dict(k, dict_phones))==None else (value_dict(k, dict_phones))) 

	print("\n".join(x for x in phone_name))

		

		

