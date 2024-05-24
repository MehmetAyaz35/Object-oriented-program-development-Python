class Car:
    wheels = 4  # Class variable
    def __init__(self, brand, model, year, color):   # Method/Function  //It does not have to be named "self" , (it can be "x" ,"a" does not matter)
        self.brand = brand  # instance variable      #you can call it whatever you like, but it has to be the first parameter of any function in the class:
        self.model = model  # instance variable
        self.year = year    # instance variable
        self.color = color  # instance variable

    def drive(self):
        print("This "+ self.model +" is driving")

    def stop(self):
        print(f"This {self.model} is stopped")
