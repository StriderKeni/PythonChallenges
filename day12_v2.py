class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):

    grade = ''

    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super(Student, self).__init__(firstName, lastName, idNumber)
        self.scores = scores    

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here

    def calculate(self):
        grade = ''
        avg = (sum(self.scores)/len(self.scores))

        if avg < 40:
            grade = 'T'
        if avg < 55:
            grade = 'D'
        if avg < 70:
            grade = 'P'
        if avg < 80:
            grade = 'A'
        if avg = 90:
            grade = 'E'
        if avg <= 100:
            grade = 'O'

        return grade
        

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())