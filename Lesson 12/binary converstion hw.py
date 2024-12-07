#binary conversion
numb = float(input (" please enter a number : " ))
s = ""

while (numb>0) : 
    rem = numb % 2
    s =  str (rem) + s
    numb = numb // 2
    print (s)
    