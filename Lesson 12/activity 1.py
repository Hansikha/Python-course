text = input ("Please enter your name : ")
c = input ("Enter the character you want to find in your name : ")
index = 0
count = 0
for i in range (index, len (text)) : 
    if text [i] == c: 
        count = count + 1
print ("the character  ", c, " has appeared for ", count," times ")