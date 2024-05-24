def save_user(**user):
    return user                # # Return allows the caller to store or use the returned dictionary for further processing.

result = save_user(name='John', age=25, city='New York')
print(result)

print("------------------------")

def save_user(**user):   # **Kwargs
    print(user)            # This version is more focused on printing the received keyword arguments rather than returning them.

save_user(name='Alice', age=30, city='London')

# result = save_user(name='Alice', age=30, city='London')
# print(result)  # this gives None. it doesn't have a return statement, so it implicitly returns None

# In summary the first version returns the dictionary, while the second version only prints the dictionary and implicitly returns None