from shopping_cart import ShoppingCart

cart1 = ShoppingCart("Mehmet")

print(cart1.__dict__)
cart1.add_item("kivi", 20)
print(cart1.items)


cart1.second_attribute = "great"
#print(cart1.second_attribute)

# Note:When I run the code of this class, the objects created in the main class will also be printed.