my_dict = {"apple": 5, "banana": 3, "cherry": 8}
# Using items() to get key-value pairs
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

my_list = [1, 2, 3]
popped_item = my_list.pop(1)  #pop(index) yazdığımız index numarası. Pop methodu yazdığım index numarasındaki item'i kaldırıyor
print(popped_item) # Result: popped_item is 2, my_list is now [1, 3]// popped_item yazdırılıyor dikkat et yani sonuç 2 olmalı

my_list.insert(8,10)  #insert(index, item)  index numarası listedekilerden fazla olursa sona ekliyor.index numarası 8'e 10 sayısını ekle.
print(my_list)


my_list1 = [1, 2, 3, 2]
index = my_list1.index(2)  #index(item) yazdığımız item. index methodu yazdığım öge(item)'nin index'ini veriyor
# Result: index is 1
print(index)



original_list = [1, 2, 3]
copied_list = original_list.copy()

# Modify the copied list
copied_list.append(4)

print(original_list)  # [1, 2, 3]
print(copied_list)    # [1, 2, 3, 4]


original_list = [1, 2, 3]
copied_list = original_list[:]

# Modify the copied list
copied_list.append(5)

print(original_list)  # [1, 2, 3]
print(copied_list)    # [1, 2, 3, 4]



