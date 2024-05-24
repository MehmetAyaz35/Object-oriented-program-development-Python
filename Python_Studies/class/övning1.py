
class Student():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

Student1 = Student("Mehmet", "Ayaz", 34)   # class içerisine yazdığım bu kısım diğer classtan import edildiğinde yazdırılır

print(Student1.first_name)
print(Student1.__dict__)
