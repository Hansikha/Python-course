def hct (a):
    '''This is a recursive function'''
    if a==0 or a==1:
        return 1
    else:
        return a * hct(a-1)
b = int(input("enter the number whose factorial you want to find out : " ))
print (hct(b))
print (hct.__doc__)