class car:
    name = "BMW" #Class Variable
    def __init__(self, colour, size):
        self.colour = colour #Instance Variables
        self.size = size
    def display_details(self):
        print("The colour of the car is ",self.colour)
        print("The size of the car is ",self.size)

o1 = car("Pink","Small")
print("The brand of the car is ",o1.name)
o1.display_details()