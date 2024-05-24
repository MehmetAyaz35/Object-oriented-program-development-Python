my_list = [1, 2, 3]

try:
    value = my_list[4]  # This will raise an IndexError since the index 4 is out of range
except IndexError as e:  # "e" here represents the error written in the terminal before specifying a special error type.Anything can be written instead of "e"
    print(f"Error: {e}")  # Error: list index out of range


# my_list2 = [1, 2, 3]

# value = my_list2[4]  # This will raise an IndexError since the index 4 is out of range
# print(f"Error: ")  # IndexError: list index out of range