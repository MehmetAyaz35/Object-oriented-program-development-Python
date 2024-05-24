class Customer():            # In object-oriented programming, a class is a blueprint for creating objects, and objects are instances of a class.
                             # When an instance of this class is created, it requires a customer_id and a product_basket (a list of products). The class also has a predefined list of allowed_products (Banana, Yoghurt, and Chocolate).
    def __init__(self, customer_id, product_basket: list):     #This is the constructor method. It is called when an object of the class is created. The self parameter refers to the instance of the class (the object being created).
        self.customer_id = customer_id
        self.product_basket = product_basket
        self.allowed_products = ["Banana", "Yoghurt", "Chocolate"]   #This line initializes an attribute named allowed_products for each object created from the Customer class.

    def add_product(self, product):   #product: This is a parameter representing the product to be added to the product_basket.
        if product in self.allowed_products:
            self.product_basket.append(product)
        else:
            raise ValueError("Product not allowed")

    def show_products(self):
        for product in self.product_basket:
            print(product)

customer_1 = Customer("12345", [])
try:
    choice = input("What product do you want to add?")
    customer_1.add_product(choice)
    customer_1.add_product("Chocolate")
except ValueError:
    print("That product is not allowed")

customer_1.show_products()




# Vi ska skapa en Customer class, tänk dig funktionalitet för att jobba med en kund för någon slags e-handlare.
# Customer ska ha ett customer ID
#Customer ska ha en lista kallad product_basket
# Customer ska ha en metod (funktion) som lägger till varor (strings) I product_basket
# Customer ska ha en metod som printar alla varor I products-listan