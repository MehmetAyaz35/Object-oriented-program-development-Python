import random

random_numbers = []

for _ in range(100):
    random_numbers.append(random.randint(1, 100))

def show_data():
    return random_numbers


def sortera_stigande():
   random_numbers.sort()
   return random_numbers

def sortera_fallande():
    random_numbers.sort(reverse=True)
    return random_numbers

def lägg_till_nummer():
    num = int(input("Skriv ett nummer att lägga till: "))
    random_numbers.append(num)
    return random_numbers


def ta_bort_specifikt_nummer():
    num = int(input("Skriv ett nummer att ta bort: "))
    if num in random_numbers:
        random_numbers.remove(num)
        return random_numbers
    else:
        print("Numret finns inte i listan.")


def ta_bort_senaste_numret():
    random_numbers.pop()
    return random_numbers

def ta_bort_första_numret():
    random_numbers.pop(0)
    return random_numbers

def sum_nummers():
    return sum(random_numbers)


while True:
    try:
        user_choice = int(input("""
        1. Visa all data i listan
        2. Sortera listan stigande
        3. Sortera listan fallande
        4. Lägg till ett nummer
        5. Ta bort ett specifikt nummer
        6. Ta bort det senaste numret
        7. Ta bort det första numret
        8. Summera alla nummer 
        """))

        if user_choice == 1:
            print(random_numbers)
        elif user_choice == 2:
            sortera_stigande()
            print(random_numbers)
        elif user_choice == 3:
            print(sortera_fallande())
        elif user_choice == 4:
            print(lägg_till_nummer())
        elif user_choice == 5:
            print(ta_bort_specifikt_nummer())
        elif user_choice == 6:
            print(ta_bort_senaste_numret())
        elif user_choice == 7:
            print(ta_bort_första_numret())
        elif user_choice == 8:
            print(sum_nummers())
        else:
            print("ogiltigt nummer! försök igen")
    except ValueError:
        print("Ogiltig inmatning! Välj ett nummer.(1-8)")