def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 5 == 0:
        return "Fizz"
    if input % 3 == 0:
        return "Buzz"


print(fizz_buzz(15))

print("-----------------------------")


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    elif input % 5 == 0:
        return "Fizz"
    elif input % 3 == 0:
        return "Buzz"
    else:
        return str(input)

print(fizz_buzz(15))

