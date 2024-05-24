# function definition
def get_square(num):
    return num * num


for i in [1,2,3]:
    # function call
    result = get_square(i)
    print('Square of',i, '=',result)

print("------------------------------")


def create_name(first,last):
    first = first.capitalize()
    last = last.capitalize()
    return first+" "+ last


full_name = create_name("mehmet","ayaz")
print(full_name)