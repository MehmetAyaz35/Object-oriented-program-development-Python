import json

book = None
while True:
    file_name = input("Choose a file name: ")
    try:
        with open(file_name, "r") as book_file:
            book = json.load(book_file)
            print(book)
            break
    except FileNotFoundError as err:
        print(err)
        print("File does not exist, try again")
    except Exception as e:
        print("Something else went wrong")