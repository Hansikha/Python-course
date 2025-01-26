def square_Value_and_filter(start, end):
 odd_square =[]
 even_square=[]
#loop through the range
 for num in range(start, end+1):
    square = num**2

    #call the square of the number
    if square %2 ==0 :
     even_square.append(square)
 else:
     odd_square.append(square)
     print("odd square values: ", odd_square)
     print("even square values", even_square)

start_range = int(input("enter the begining number of the range: "))
end_range = int(input("Please enter the ending number of the range: "))
square_Value_and_filter(start_range, end_range)
