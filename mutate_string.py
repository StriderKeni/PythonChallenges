def mutate_string(string, position, character):
	list_string = list(string)
	list_string[position] = character
	return "".join(list_string)

	#new_string = string[:position] + "character" + string[position:]
	#return new_string


if __name__ == '__main__':
	s = input()
	i, c = input().split()
	s_new = mutate_string(s, int(i), c)
	print(s_new)