import math
import os
import random
import re 
import sys

def percent(x, percent):
	total = x*percent/100
	return total

if __name__ == '__main__':
	meal_cost = float(input())
	tip_percent = int(input())
	tax_percent = int(input())

	total_tip = percent(meal_cost, tip_percent)
	total_tax = percent(meal_cost, tax_percent)

	total_meal = meal_cost+total_tip+total_tax
	print("Your total meal cost is: {}".format(int(round(total_meal, 0))))


