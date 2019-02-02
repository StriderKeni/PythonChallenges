import string

def solve(s):
	#return s.title() falla al juntar por ejemplo una palabra 3g -> 3G
	#new_string = ' '.join(w[0].upper() + w[1::] for w in s.split(' ')) -> No funcionó para todos los casos, pero de todas maneras sigue siendo un metodo valido
	#return new_string
	return string.capwords(s, ' ')

if __name__ == '__main__':

	s = input()
	str1 = solve(s)

	print(str1)



