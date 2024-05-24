def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


# Keyword argument need to follow positional argument
hello("Hello", first="Mehmet", last="Ayaz", title="Mr")  # Hello Mr Mehmet Ayaz

