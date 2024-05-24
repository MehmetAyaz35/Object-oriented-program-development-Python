import json

# some JSON:                          #If you have a JSON string, you can parse it by using the json.loads() method.
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y)
print(y["age"])
