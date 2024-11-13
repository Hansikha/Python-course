#identity operators
x = 10
y = 10
z = 20
if x is y :
    print ("true")
else :
    print ("false")

if y is not z :
    print ("y and z do not hold the same value")
else :
    print ("y and z share the same value")
#membership operators
a = "rainbows"
b = "rain"
c = "cats"
if b in a :
    print (b," is present in ",a )
elif c not in a :
    print (c," is not present in ",a )


