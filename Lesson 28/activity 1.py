class IOstring:
    def __init__(self):
        self.str1 = ""
    def get_string (self):
        self.str1 = input("Please enter a string: ")
    def print_string (self):
        print("The entered string in upper class is ",self.str1.upper())
object1 = IOstring()
object1.get_string()
object1.print_string()