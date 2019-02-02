class Person():
	"""docstring for Person"""
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber

	def __str__(self):
		return "Name: {}, {}\nID: {} ".format(self.lastName, self.firstName, self.idNumber)


class Student(Person):
	"""docstring for Student"""

	def __init__(self, firstName, lastName, idNumber, array):
		super(Student, self).__init__(firstName, lastName, idNumber)
		self.array = array

	def calculator(self):
		grade = ''
		score = int(sum(self.array)/len(self.array))
		if score in range(90,101):
			grade = 'O'
		if score in range(80,90):
			grade = 'E'
		if score in range(70, 80):
			grade = 'A'
		if score in range(55, 70):
			grade = 'P'
		if score in range(40, 55):
			grade = 'D'
		if score < 40:
			grade = 'T'
			
		return grade


	def result(self):
		print("Name: {}, {}".format(self.lastName, self.firstName))
		print("ID: {}".format(self.idNumber))
		
if __name__ == '__main__':
	eugenio = Student(input().strip(),input().strip(), input().strip(), list(map(int, input().rstrip().split())))
	eugenio.result()
	eugenio.calculator()