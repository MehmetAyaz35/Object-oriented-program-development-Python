from car_class import Car

car_1 = Car("Toyota", "Mustang", 2020, "Blue")
car_2 = Car("Mercedes", "E200", 2023, "Black")

print(car_1.__dict__)   # {'brand': 'Toyota', 'model': 'Mustang', 'year': 2020, 'color': 'Blue'}
print(car_1.brand)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive()   # . ile variable ekleyebilirim
car_2.stop()


car_1.wheels = 3    # I assigned new value for car_1.wheels
print(car_1.wheels)
print(car_2.wheels) # Default value from the car_class

Car.wheels = 6

print(car_1.wheels)   # Why is it still 3? Answer is below
print(car_2.wheels)

# In your code, wheels is a class variable shared by all instances of the Car class. When you do car_1.wheels = 3, you are creating an instance
# variable wheels for the specific instance car_1, which shadows the class variable wheels for that instance.

# So, when you later do Car.wheels = 6, it changes the class variable for all instances except for car_1, because it has its own instance variable
# wheels with a value of 3.