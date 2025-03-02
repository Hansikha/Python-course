class dog:
    animal = "dog"

    def __init__ (self, breed, colour):
        self.breed = breed
        self.colour = colour
    def dog_details(self):
        print("The dog's breed is:" ,self.breed)
        print("The dog's colour is:" ,self.colour)


DogA = dog("pug", "brown")
DogB = dog("poddle", "white")

DogA.dog_details()
DogB.dog_details()
