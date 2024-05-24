def my_function(*kids):                         #If the number of arguments is unknown, add a * before the parameter name:
    print("The youngest child is " + kids[2])   #Look print_return class (There is more information)


my_function("Emil", "Tobias", "Linus")


def my_function2(**kid):  # **Kwargs
    print("His last name is " + kid["lname"])


my_function2(fname = "Tobias", lname = "Refsnes")