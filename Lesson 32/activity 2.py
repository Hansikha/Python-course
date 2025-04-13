#write a program to create a quiz related to multiple fruits using object-oriented programming in Python. Create a class that consists of -1. a constructor with a dictionary of fruits and respective colours 2.a function to execute the quiz. Here,the fruit will be chosen at random from the dicitionary. Then ask the user to enter the colour of that fruit. Evaluate the answer and display the result accordingly

import random
class fruit_quiz:
    def __init__(self):
        self.fruits = {"dragon fruit":"white", "pineapple":"yellow", "blueberry":"blue", "watermellon":"red", "rasberry":"pink"}
    def quiz(self):
        while (True):
            fruit, colour = random.choice(list(self.fruits.items()))
            print("Hi! What is the colour of {}".format(fruit))
            user_answer = input()

            if(user_answer.lower() == colour):
                print("Congratulations! Your answer is correct!")
            else:
                print("Unfortunetly. Your answer is incorrect.")

            replay = int(input("press 0 , if you want to play again but if you dont please press 1: "))
            if (replay):
                break

print("Hello! Welcome to this quiz about fruits!")
frq = fruit_quiz()
frq.quiz()

