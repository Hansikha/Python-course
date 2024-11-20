cause = input ("enter if you have a medical condition as Y or N :")
attendence = int (input("please enter the percentage of your attendence"))
if cause == "Y" :
    print ("you are allowed to take the test")
else: 
    if attendence >= 75 :
         print ("you are allowed to take the test")
    else:
        print ("you are not allowed to take the test")

