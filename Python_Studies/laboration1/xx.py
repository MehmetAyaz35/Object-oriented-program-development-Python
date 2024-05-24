students = [
    {'name': 'John', 'age': 18, 'passed': True, 'major': 'computer science', 'GPA': 3.8},
    {'name': 'Jane', 'age': 19, 'passed': False, 'major': 'biology', 'GPA': 3.2},
    {'name': 'Bob', 'age': 20, 'passed': True, 'major': 'engineering', 'GPA': 3.5},
    {'name': 'Alice', 'age': 21, 'passed': False, 'major': 'history', 'GPA': 2.9},
    {'name': 'David', 'age': 22, 'passed': True, 'major': 'business', 'GPA': 3.6}
]

succesful_students =[]

for student in students:
    if student["passed"]:
        succesful_students.append(student)

print(succesful_students)