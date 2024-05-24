car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "year" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")