dict_1 = {"Codingal":3,"is":2,"best":2,"for":2,"Coding":1}
print (dict_1)
a = 2
b = 0
for key in dict_1:
    if dict_1[key] == a:
        b = b + 1

print("The frequency is " + str(b))