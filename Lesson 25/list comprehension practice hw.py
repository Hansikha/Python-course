#1 Take a number from the user, create a list with all the odd numbers uner the input value and another list of odd numbers.
#2 create a list of fruits. Then, convert the first letter of every elemetn to capital and create a new list of updated values

number = int(input("enter a number: "))
odd_number =[x for x in range(number)
             if x %2 ==1]
print("odd number less than", number, "are:", odd_number)

# task 2
fruits =["apple", "banana","mango", "grapes"]
updated_fruits = [fruit.capitalize()
                 for fruit in fruits]
print("updated fruits list: ", updated_fruits)







