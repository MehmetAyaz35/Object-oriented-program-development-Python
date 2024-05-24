# define a class
class Bike:
    name = ""
    gear = 0

# create object of class
bike1 = Bike()
bike2 = Bike()

# access attributes and assign new values
bike1.gear = 11
bike1.name = "Mountain Bike"

bike2.gear =21
bike2.name = "Bianchi"

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")
print(f"Name: {bike2.name}, Gears: {bike2.gear} ")