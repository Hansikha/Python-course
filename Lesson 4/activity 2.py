amount = int(input("Hi! Please enter the amount for withdraw :"))

note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("notes of 100 pounds" , note1)
print("notes of 50 pounds" , note2)
print("notes of 10 pounds" , note3)