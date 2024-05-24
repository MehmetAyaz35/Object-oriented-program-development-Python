# In Python, __init__ is a special method, also known as the "initializer" or "constructor," that is automatically called when an object
# is created from a class. The __init__ method allows you to perform any necessary setup or initialization of the object.
class MyClass:
    def __init__(self, parameter1, parameter2):
        # Initialization code here
        self.parameter1 = parameter1
        self.parameter2 = parameter2
        # Other initialization tasks if needed

# Creating an instance of MyClass
obj = MyClass("value1", "value2")


# In this example, when you create an instance of MyClass (e.g., obj), the __init__ method is automatically called, and it initializes the
# object with the provided values for parameter1 and parameter2. The self parameter refers to the instance of the class, and it is automatically
# passed when you create an object.

# Using __init__ allows you to set up the initial state of your objects and provide default values or parameters during object creation.
# This method is fundamental in object-oriented programming and is commonly used to ensure that the object is in a valid state upon creation.