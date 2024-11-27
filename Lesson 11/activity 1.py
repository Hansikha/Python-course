# finding the sum of natural numbers
b = 1
a = int(input("Please enter a number : "))
sum = 0
while b <= a:
    sum = sum + b
    b = b + 1
    print ("sum is ", sum)