import os
a = input("would you like to shut down your computer? yes/no: ") 
if a == 'no':
    exit()
else: 
    b = input("do you have any unsaved peices of work? yes/no: ")
if b == 'yes':
    exit()
else:
    os.system("shutdown /s /t 1") 