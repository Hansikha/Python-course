t = int(input("Please enter a numerator: "))
g = int(input("Please enter a denominator: "))
try:
    if g == 0:
        raise ZeroDivisionError
    else:
        print(g)
    print (t/g)
except ZeroDivisionError:
    print ("The numerator is not divisble by 0")
finally:
    print("This is the end")
