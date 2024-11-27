a = int(input ("enter a number 11 :"))
temp = a
sum = 0
while temp > 0:
    c = temp % 10
    sum += c **3
    temp = temp // 10
if a == sum:
    print ("This is an amstrong number")
else:
    print ("This is not an amstrong number")