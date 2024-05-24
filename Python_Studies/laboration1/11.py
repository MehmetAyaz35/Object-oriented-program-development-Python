student_grades = {
    9210114413: {"grade": 55, "passed": True},
    9010054514: {"grade": 22, "passed": False},
    8504129392: {"grade": 60, "passed": True},
    9201134555: {"grade": 15, "passed": False},
}

students_to_remove = []
for student_id, student_info in student_grades.items():
    if student_info["passed"] == True:
        students_to_remove.append(student_id)
print(students_to_remove)

for student_id in students_to_remove:
    del student_grades[student_id]

print(student_grades)


#"in" is the keyword used to specify the list (or any other iterable) over which the loop should iterate.
#So "in" here acts as a join between the keyword "for", the temporary variable name "name" and the list to be iterated over, "names".
#It allows the loop to go through each element of the list one by one and perform the specified action for each element.

#Here "in" is inside a condition .This condition determines whether the name should be included in the new list based on whether the name contains the string "to".
'''
def return_first_negative_number(l):
    for number in l:
        if number < 0:
            return number
'''

def return_first_negative_number(l):
    negative_number = []
    for number in l:
        if number < 0:
            negative_number.append(number)
            break
    return negative_number

numbers_list = [4, 1, 34, 42, -20, 21, 49, -48, 40, 3, -21, 10, 37, 36]
print(return_first_negative_number(numbers_list))

def find_negative_numbers(l):
    negative_numbers = []
    for number in l:
        if number < 0:
            negative_numbers.append(number)
    return negative_numbers

numbers_list = [4, 1, 34, 42, -20, 21, 49, -48, 40, 3, -21, 10, 37, 36]
print(find_negative_numbers(numbers_list))








