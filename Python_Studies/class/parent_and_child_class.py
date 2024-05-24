class Person:    # Parent class
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

class Student(Person):   # Child class
    pass                 # Note: Use the pass keyword when you do not want to add any other properties or methods to the class

y = Student("Mike", "Olsen")
y.printname()
