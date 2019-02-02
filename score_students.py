n = int(input())
students = []

for i in range(n):
    grade = [input(), float(input())]
    students.append(grade)

students = sorted(students, key= lambda x: x[1])
second_highest = students[0][1]

for name, grade in students:
    if grade > second_highest:
        second_highest = grade
        break

print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))





'''def sortValue(val):
    return val[1]

if __name__ == '__main__':
    
    list_score = []
    order_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_score.append((name, score))
   
    list_score.sort(key= sortValue, reverse = False) # Order the list for the second value of a tuple
    
    first_element = (list_score[0])

    order_list = [(ele1,ele2) for ele1, ele2 in list_score if ele2!=list_score[0][1]]

    list_score.remove(list_score[0]) # We don't need the first element so I remove it.

    order_list.sort()

    print(order_list)
    print(list_score)

    if order_list[0][1] ==  order_list[1][1]:
        print(order_list[0][0]) #list with alphabetical order
        print(order_list[1][0]) #list with alphabetical order
    else:
        print(list_score[0][0]) #list withouth alphabetical order'''



