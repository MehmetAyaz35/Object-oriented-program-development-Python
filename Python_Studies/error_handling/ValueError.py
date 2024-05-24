# ValueError is a common exception in Python that occurs when a function receives an argument of the correct type but with an invalid value.
def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")      # tabi ki return'den önce olmalı
    return a / b

# Example usage

try:
    result = divide_numbers(10, 0)
except ValueError as ve:    # The choice of variable name after as in the except block is entirely up to you. The variable name is just a way to refer to the exception object within the except block. While as e is a common convention (where "e" often stands for "exception"), you can choose any valid variable name that makes sense to you.in example vg
    print(f"Error: {ve}")   # Error: Cannot divide by zero
else:
    print(f"Result: {result}")

