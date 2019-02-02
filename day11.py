
import math
import os
import random
import re
import sys



if __name__ == '__main__':
		arr = []

		for _ in range(6):
			arr.append(list(map(int, input().rstrip().split())))
    
		sum_hourglass = 0

		for i in range(4):
			for j in range(4):
				temp_sum = (arr[i][j]+arr[i][j+1]+arr[i][j+2])+(arr[i+1][j+1])+(arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])	
				if temp_sum > sum_hourglass:
					sum_hourglass = temp_sum

		print(sum_hourglass)



'''
max_total = True
for i in range(len(arr) - 2):
    for j in range(len(arr[i]) - 2):
        total = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
        if max_total == True:
            max_total = total
        max_total = max(max_total, total)
print(max_total)
'''