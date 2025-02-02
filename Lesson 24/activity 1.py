#Making a set with integers
s1 = {1,2,3,4,5}
print(s1)
#Making a set with mixed data elements
s2 = {1,"Coding",2.2}
print(s2)
s3 = {1,2,3,4,3,2}
print(s3)
#Making a set from a list
s4 = [1,2,3,4,5]
s5 = set(s4)
print(s5)
#Print a set after removing an element using pop
s6 =set([0,1,3,4,5])
s6.pop()
print(s6)
#inetection on a set
s7 ={1,2,8,5,6}
s8 = {8,5,1,3,6,9}
print(s7.intersection(s8))
