# try:
#    a=int(input("enter the number :  "))
#    print(a)
# except Exception as e:
#   print("exception :",e)



# try:
#    a=int(input("enter the number :  "))
#    print(a)

# except ValueError as v:
#    print("hey")
#    print(v)   
# except Exception as e:
#   print("exception :",e)  
 


#  RAISING EXCEPTIONS
a=int(input("enter the 1st number: "))
b=int(input("enter the 2nd number: "))
if(b==0):
    raise ZeroDivisionError("number is not divide the zero")
else:
   print(f"the division a/b is : {a/b}")



# TRY WITH ELSE CLAUSE 
try:
   a=int(input("enter the number :  "))
   print(a)

 
except Exception as e:
  print("exception :",e)

else:    # This is executed only if the try was successful
   print("i am inside else")  



#    TRY WITH FINALLY
try:
   a=int(input("enter the number :  "))
   print(a)

 
except Exception as e: 
  print("exception :",e)

finally:    # This is executed always
 print("i am inside finally")  
 

def main():
   try:
    a=int(input("enter the number :  "))
    print(a)
    return

   except Exception as e: 
    print("exception :",e)
    return

   finally:    # This is executed permanelty return rahe ya na rhe
    print("i am inside finally")  
main()    
 




