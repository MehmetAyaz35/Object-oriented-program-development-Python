import json   #If I do not import json, json in the code will not be defined.

data = {
    "name": "Hakan",
    "age": 30,
    "city": "New York",
    "country": "USA"
}


# Without sorting the keys
json_str = json.dumps(data)
print(json_str)

# With sorting the keys
json_str_sorted = json.dumps(data, sort_keys=True)    # The sort_keys parameter is a boolean that, if set to True, specifies that the keys in the resulting JSON object should be sorted in alphabetical order.d
print(json_str_sorted)
