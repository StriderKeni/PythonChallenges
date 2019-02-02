from collections import OrderedDict, defaultdict, Counter

string = sorted(input())


for each in Counter(string).most_common(3): 

	print(string)
	print(*each)



'''if __name__ == '__main__':
    s = input()
    for char in s:
        default_dict[char] += 1
    
    sorted_dict = {v: k for k,v in sorted(default_dict.items(), key= lambda x: x[1]) }
    reverse_dict = OrderedDict(list(sorted_dict.items())[::-1])



    for key, value in reverse_dict.items():
        print("{} {}".format(value, key))'''
 
