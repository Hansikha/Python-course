a = int(input("Please enter your age: "))
try:
    if type(a) is not int:
        raise ValueError
    else:
        if a % 2 == 0:
            print("This number is an even number: ")
        else:            
            print("This number is an odd number: ")
except ValueError:
    print ("We only accept numbers")
finally:
    print("The end")




    