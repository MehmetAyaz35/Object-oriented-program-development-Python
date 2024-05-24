import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))     # print(json.dumps(x, indent=4, separators=(". ", " = ")))    * You can also define the separators, default value is (", ", ": ")
"""
Python	    JSON
dict	    Object      
list     	Array
tuple	    Array
str	        String
int	        Number
float	    Number
True	    true
False	    false
None	    null
"""
