def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

print("---------------------------")


def save_user(**user):
    return user  # user["name"]  if you write this content you just get result as a name


presentation = save_user(id=2, name="Hanna", age=28)
print(presentation)

print(
    "--------------------------------")  # So, the main difference between the two code snippets is that the first one returns the user dictionary, while the second one only prints it to the console.


def save_user(**user):
    print(user)


# Since there is already print in the function we defined, I do not need to write it again.My comment
save_user(id=2, name="hakan", age=18)
