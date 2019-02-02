#	Declare 3 variables (i,d,s), int, double, string.
# Read the input of those 3 variables

# Print i+s on a new line
# D+ double variable to a scale of one decimal place on a new line
# Concatenate S with the string you read as input and print the result on a new line.


i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
var_int = int(input())
var_double = float(input())
var_string = input()

# Read and save an integer, double, and String to your variables.
var_int = var_int + i
var_double = d + var_double
var_string = s + var_string

# Print the sum of both integer variables on a new line.
print(var_int)
# Print the sum of the double variables on a new line.
print("{:.1f}".format(var_double))
# Concatenate and print the String variables on a new line
print(var_string)
# The 's' variable above should be printed first.

