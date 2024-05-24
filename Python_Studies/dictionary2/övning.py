import random

random_numbers = []

for _ in range(100):
    random_numbers.append(random.randint(1, 100))
def show_data():
    return random_numbers


def sortera_stigande():
    show_data()
    return random_numbers.sort()

def sortera_fallande():
    show_data()
    random_numbers.sort(reverse=True)

def lägg_till_nummer():
    show_data()
    num = int(input("Skriv ett nummer att lägga till: "))
    random_numbers.append(num)

def ta_bort():
    show_data()
    num = int(input("Skriv ett nummer att ta bort: "))
    if num in random_numbers:
        random_numbers.remove(num)
    else:
        print("Numret finns inte i listan.")


def ta_bort_senaste_numret():
    show_data()
    random_numbers.pop()

def ta_bort_första_numret():
    show_data()
    random_numbers.pop(0)

def sum_nummers():
    show_data()
    total = sum(random_numbers)
    print("Total är: ", total)

#show_data()
#sortera_fallande()
lägg_till_nummer()
#sum_nummers()
print(random_numbers)




