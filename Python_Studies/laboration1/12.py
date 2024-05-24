student_grades = {
    9210114413 : {"grade": 55, "passed": True},
    9010054514 : {"grade": 22, "passed": False},
    8504129392 : {"grade": 60, "passed": True},
    9201134555 : {"grade": 15, "passed": False},
}


new_dict_of_student_grades = {}

for student_personnumber, student_result in student_grades.items():
    if student_result["passed"] == False:
        new_dict_of_student_grades[student_personnumber] = student_result


print(new_dict_of_student_grades)

