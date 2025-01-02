def sub(price, pay):
    return price - pay

price = float(input("Enter the total cost of the things you bought today: "))
print("You owe", price)
pay = float(input("Enter the amount of money you will be paying today: "))
s = sub(price, pay)
print("The amount left on your tab is", s)










