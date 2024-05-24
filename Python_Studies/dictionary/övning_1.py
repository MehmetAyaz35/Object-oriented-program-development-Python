def greet(first_name,last_name):
    #Parameters ;is the input that you defined for your function
    print(f"Hi {first_name} {last_name}\nWelcommen")

#Arguments . is the actual value for a given parameter
greet("Mehmet","Ayaz")

print("----------------------------------")

def greeting(name):
    print(f"hi {name}")

greeting("Mehmet")  #hi Mehmet
#Optional Return Value: Functions in Python can also have no "return" statement or can simply use "return" without specifying a value. In such cases, the function returns a special value called None, which indicates the absence of a meaningful result.
print(greeting("Mehmet")) #None

print("-------------------------------------")

def greeting(name):
    result = f"hi {name}"
    return result                #or only    return f"hi {name}" instead of last two code block
#Using the Returned Value: When you call a function that includes a "return" statement, you can capture the returned value and use it in your code.
sentence = greeting("Mehmet")
print(sentence)                 #hi Mehmet  or only   print(greeting("Mehmet")) instead of last two block