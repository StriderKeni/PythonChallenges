'''
*
You are driving a little too fast, and a police officer stops you. 
Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". 
If your speed is 60 or less, the result is "No Ticket". 
If speed is between 61 and 80 inclusive, the result is "Small Ticket". 
If speed is 81 or more, the result is "Big Ticket". 
Unless it is your birthday (encoded as a boolean value in the parameters of the function) 

-- on your birthday, your speed can be 5 higher in all cases. 
*
'''

def caught_speeding(speed, birthday):

	if birthday==True:
		if speed <= 60:
			return "No Ticket"
		elif speed in range(61*5, 80*5):
			return "Small Ticket"
		else:
			return "Big Ticket"
	else:
		if speed <= 60:
			return "No Ticket"
		elif speed in range(61, 81):
			return "Small Ticket"
		elif speed > 81:
			return "Big Ticket"

if __name__ == '__main__':
	speed_user = caught_speeding(81, False)

	print(speed_user)


