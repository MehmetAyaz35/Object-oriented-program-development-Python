class StudentManagementSystem:
    def __init__(self, students=None):

        if students is not None:
            self.students = students
        else:
            self.students = {}


        self.available_courses = ["Math", "English", "Programming"]
        self.available_grades = ["A", "B", "C", "D", "E", "F"]

    def add_student(self, student_id, student_info):


        if student_id in self.students:
            raise ValueError("Student ID already exists")
        self.students[student_id] = student_info