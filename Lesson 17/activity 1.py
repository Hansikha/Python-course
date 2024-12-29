#using break keyword
b = input("Please enter a word: ")
for i in b:
    #print(i)
    if i == "a":
        print("There is an a in the word you have written: ")
        break
    else:
        print("There is no a in the word you have written: ")

#using return keyword
def add (a,b):
    return a+b
s = add(10,20)
print (s)

#using continue keyword
h = 10
while h > 0:
    h = h - 1
    if h == 6:
        continue
    print ("The value of h is ",h)
    
