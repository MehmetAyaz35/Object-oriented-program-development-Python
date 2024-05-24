class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) # John(36)   // if i do not create __str__ function above ,i would get <__main__.Person object at 0x000001A7B926C8D0> as a result