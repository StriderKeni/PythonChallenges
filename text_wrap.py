
import textwrap

def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


# if __name__ == '__main__':
# 	string = input()
# 	split_string = [ string[i:i+4] for i in range(0, len(string), 4)]
# 	print(*split_string)

# def wrap(string):
# 	split_string = []
# 	for i in range(0, len(string),4):
# 		split_string.append(string[i:i+4])

# 	return split_string

# if __name__ == '__main__':
# 	string = input()

# 	print(*wrap(string))

