dict_1 = {"Codingal":3,"is":2,"best":2,"for":2,"Coding":1}
print (dict_1)
a = (input("Hi! Enter the value you want to check the frequency of: "))

b = 0
for res in dict_1:
    print(res)
    if dict_1[res] == a:
        b = b + 1
        print("The frenquency of your choosen value is : " + str(b))
    else:
        