a = 25
b = 10
c = 5
d = 30
e = 15

exp = (d + e) / c * b
print (exp)

exp1 = a + (d -((c-e) * b)) + a**c
print (exp1)

#Activity 2
name = "bob1"
age = 10
if name == "bob" or name == "john" and age <15 :
    print ("Hello, how are you")
else :
    print ("Goodbye")

#Activity 3 
print ("enter a numerator") 
nn = int (input ())
print ("enter a denominator")
na = int (input ())
if nn%na == 0 :
    print (nn, " is divisable by ",na)
else :
    print (nn, " is not divisble by ",na)