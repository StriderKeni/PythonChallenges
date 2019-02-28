
t = int(input())
final_complements = []

for t_itr in range(t):

	n, k = map(int, input().split())

	max_input = 0

	for x in range(1, n+1):
		for a in range(x+1, n+1):
			if x&a > max_input and x&a < k:
				max_input=x&a


	final_complements.append(str(max_input))


print("\n".join(final_complements))





