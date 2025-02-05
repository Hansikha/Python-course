def square(h):
    return h**2
numb = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = map(square,numb)
print (list(a))

b = [1,2,3,4,5]
c = [6,7,8,9,10]
d = map(lambda  x,y:x+y,b,c)
print (list(d))

