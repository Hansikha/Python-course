h = 10
i = 5
print(h)
print(i)
try:
    print(a)
    raise NameError
except NameError:
    print ("a is not defined")
print (h+i)