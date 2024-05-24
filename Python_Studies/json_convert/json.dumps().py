import json

# a Python object (dict):           #If you have a Python object, you can convert it into a JSON((JavaScript Object Notation)) string by using the json.dumps() method.
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)