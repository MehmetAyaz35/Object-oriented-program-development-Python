thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})   # Aşağıdaki örnek ile aynı mantık tek bir girdi var.key olarak "year" ve sonra : value kısmı
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# thisdict["year"].update({"2030"})  # AttributeError: 'str' object has no attribute 'update'. Bunu yazdırdığım zaman bu hatayı alırım çünkü;
                                          # The update method is used for updating the dictionary with elements from another dictionary, not for updating a specific value within a dictionary.
                                          # "year":{1: 1964} örneğin bu şekilde olsaydı doğru olurdu.
#The update() method will update the dictionary with the items from the given argument.
# The argument must be a dictionary, or an iterable object with key:value pairs.

thisdict["year"] = 2023   # You can change the value of a specific item by referring to its key name. This is the correct usage
print(thisdict)  # {'brand': 'Ford', 'model': 'Mustang', 'year': 2023}


thisdict.update({"color": "red"})   # The update() method will update the dictionary with the items from a given argument.*** If the item does not exist, the item will be added***
print(thisdict)


StudentManagementSystem = {
        "001": {"name": "Alice", "age": 20, "grades": {"Math": "A", "English": "B"}},
        "002": {"name": "Bob", "age": 22, "grades": {"Programming": "B", "English": "A"}},
    }
print(StudentManagementSystem)

StudentManagementSystem["001"].update({"age": 21, "grades": {"Math": "B", "English": "A"}})
print(StudentManagementSystem)

StudentManagementSystem.update({"003":{"age": 40, "grades": {"Math": "C", "English": "C"}}})  # Esasında update methodu ile bir değer veya öge eklememiz gerekiyor.Örnekte sadece 1 dict ekledim.Ve eğer güncelleme yapacağımız "key" sözlükte yoksa bu şekilde yapmalıyız.yukarıdaki 2 örnek farklı dikkat et.
print(StudentManagementSystem)

