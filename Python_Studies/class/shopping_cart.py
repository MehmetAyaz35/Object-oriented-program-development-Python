# Assuming you have a ShoppingCart class
class ShoppingCart:

    #new_attribute = "Some value"      # if i want to add this attribute in class and call the this attribute (new_attribute) from the other class so be careful indentation

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.new_attribute = "Some value"  # Burada yazarsam objede otomatik olarak görünür fakat yukarıdaki şekliyle eklersem özelliği çağırmam gerekir
        print("This text comes from the imported class")
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        return self.items  # Add this line to return the updated items list

'''
# Create an object
cart = ShoppingCart("John Doe")

# Add a new attribute by using the dot(.) notation.
cart.new_attribute = "Some value"

# Access the new attribute
print(cart.new_attribute)  # Output: Some value

print(cart.__dict__)  # {'customer_name': 'John Doe', 'items': [], 'new_attribute': 'Some value'}


print(cart.add_item("Kivi", 20))  # [{'item': 'Kivi', 'price': 20}]
print(cart.__dict__)              # {'customer_name': 'John Doe', 'items': [{'item': 'Kivi', 'price': 20}], 'new_attribute': 'Some value'}
'''