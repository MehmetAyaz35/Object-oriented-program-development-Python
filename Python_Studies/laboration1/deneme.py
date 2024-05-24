import random

random_numbers = []

def generate_random_numbers():
    for _ in range(100):
        random_numbers.append(random.randint(1, 100))

def show_data():
    print(random_numbers)

def sort_ascending():
    random_numbers.sort()
    random_numbers

def sort_descending():
    random_numbers.sort(reverse=True)

def add_number():
    num = int(input("Ange ett nummer att lägga till: "))
    random_numbers.append(num)

def remove_specific_number():
    num = int(input("Ange ett nummer att ta bort: "))
    if num in random_numbers:
        random_numbers.remove(num)
    else:
        print("Numret finns inte i listan.")

def remove_latest_number():
    if random_numbers:
        random_numbers.pop()
    else:
        print("Listan är tom.")

def remove_first_number():
    if random_numbers:
        random_numbers.pop(0)
    else:
        print("Listan är tom.")

def sum_numbers():
    total = sum(random_numbers)
    print("Summan av alla nummer är:", total)

generate_random_numbers()

while True:
    user_choice = int(input("""
    1. Visa all data i listan
    2. Sortera listan stigande
    3. Sortera listan fallande
    4. Lägg till ett nummer
    5. Ta bort ett specifikt nummer
    6. Ta bort det senaste numret
    7. Ta bort det första numret
    8. Summera alla nummer 
    9. Avsluta programmet
    """))

    if user_choice == 1:
        show_data()
    elif user_choice == 2:
        sort_ascending()
    elif user_choice == 3:
        sort_descending()
    elif user_choice == 4:
        add_number()
    elif user_choice == 5:
        remove_specific_number()
    elif user_choice == 6:
        remove_latest_number()
    elif user_choice == 7:
        remove_first_number()
    elif user_choice == 8:
        sum_numbers()
    elif user_choice == 9:
        break
    else:
        print("Ogiltigt val. Försök igen.")
