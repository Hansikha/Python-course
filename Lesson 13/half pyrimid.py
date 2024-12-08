#half pyrimid pattern by taking an input from a user
r = int(input("please enter the amount of rows you want : "))
for index in range(r):
    for columns in range(index + 1):
        print("*", end = " ") 
    print ("")
#Floyds Triangle
n = int(input("write the number of rows : "))
number = 1
for i in range(1, n + 1):
    for c in range(1, i + 1):
        print(number, end = " ")
        number = number + 1
    print ("")