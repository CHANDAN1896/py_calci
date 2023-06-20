
print("enter 1 for sum(+)")
print("enter 2 for div(/)")
print("enter 3 for mul(*)")
print("enter 4 for sub(-)")
c = int(input(" what you have to do sum(+),div(/),mul(*),sub(-) choose by number given above = "))
while c<=4:
   a=int(input("Enter first no : "))
   b=int(input("Enter second no : "))

   if c == 1:
      print("addition of the numbers given are : ",a+b)
   elif c == 2:
      print("division of the given numbers are :",a/b)
   elif c == 3:
      print("multiplication of the given numbers are :",a*b)
   elif c == 4:
      print("substraction of the given numbers are :",a-b)
   else:
      print("Please enter a valid input")
   if c>=5:
        break
print("please enter valid input")
       
    
    
