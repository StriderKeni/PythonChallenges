#Student Grades

n = int(input("Ingresa la cantidad de estudiantes: "))
student_marks = {}

for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))

	student_marks[name] = scores

query_name = input()
avg_student = sum(student_marks[query_name], 0.0)/float(len(student_marks[query_name]))
print("%.2f" %avg_student)

'''
from decimal import Decimal

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    query_scores = student_marks[query_name]
    # Sum the scores in the list: total_scores
    total_scores = sum(query_scores)

    # Convert the floats to decimals and average the scores: avg
    avg = Decimal(total_scores/3)
    # Print the mean of the scores, correct to two decimals
    print(round(avg,2))
'''






