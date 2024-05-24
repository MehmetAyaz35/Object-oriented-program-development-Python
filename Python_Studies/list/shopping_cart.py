# Create an empty shopping cart
shopping_cart = []

# Add items to the shopping cart
shopping_cart.append("Apples")
shopping_cart.append("Bananas")
shopping_cart.append("Milk")
shopping_cart.append("Bread")

# Display the items in the shopping cart
print("Items in the shopping cart:")
for item in shopping_cart:
    print(item)

# Remove an item from the shopping cart
item_to_remove = "Bananas"
shopping_cart.remove(item_to_remove)

# Display the updated items in the shopping cart
print("\nUpdated items in the shopping cart:")
for item in shopping_cart:
    print(item)