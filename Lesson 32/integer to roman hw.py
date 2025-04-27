#INTERGER TO ROMAN
import random
class Roman_Numeral:
    def __init__(self):
        self.roman = {1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX", 10:"X"}
    def quiz(self):
        while (True):
                roman, integer = random.choice(list(self.roman.items()))
                print("What is the roman digit of {}".format(roman))
                user_reply = input()
                print(integer)
                if (user_reply == integer):
                     print("Congrats!!! Your answer is correct!!!")
                else:
                     print("Unfortunetly! Your answer is incorrect!")

                replay = int(input("please press 0 if you want to play again otherwise if you want to stop playing please press 1: "))
                if (replay):
                     break
                
print("Hi!! Welcome to guess the roman numeral")
rn = Roman_Numeral()
rn.quiz()
