class Student():    # In Python 2, the use of parentheses was required when defining a class, but it is not necessary in Python 3. Both syntaxes are valid in Python 3

    def full_name(self):
        return self.first_name + " " + self.last_name

    def print_full_name_and_age(self):
        print(f"My name is {self.full_name()} and I am {self.age} years old")

    def send_email(self):
        pass

student_1 = Student()
student_1.first_name = "Tobias"
student_1.last_name = "Fors"
student_1.age = 30

student_2 = Student()
student_2.first_name = "Alfred"
student_2.last_name = "Holm"
student_2.age = 25

students = []
students.append(student_1)
students.append(student_2)

for student in students:
    student.print_full_name_and_age()
