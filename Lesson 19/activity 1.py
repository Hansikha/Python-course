import random
playing = True
a = random.randint(0,10)
while playing:
    print("Please guess a number between 0 and 10: ")
    b = int(input("Enter the number you want to guess: "))
    if b==a:
        print("The number you have guessed is ",b)
        print("Great Job!!! You have guessed the correct number")
        playing = False
    else:
        print("The number you have guessed is ",b)
        print("Oh No!!! You have guessed the incorrect number")
        
