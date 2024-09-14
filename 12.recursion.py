# factorial
# def fact(i):
#     if (i==0 or i==1):
#       return 1
#     else:
#        return i*fact(i-1)
    
# i=int(input("enter the number: "))
# print(fact(i))    


    # practice

# Write a program using functions to find greatest of three numbers
# def great(a,b,c):
#   if(a>b and a>c):
#      return a
#   elif(b>a and b>c):
#      return b
#   else:
#      return c
# a=int(input("enter the num1: "))
# b=int(input("enter the num2: "))
# c=int(input("enter the num3: "))
# print(great(a,b,c))



# Write a python program using function to convert Celsius to Fahrenheit.
# c/5=(f-32)/9

# def temp(f):
#    return 5*(f-32)/9
# f= int (input("enter the F : "))
# print(f"{round(temp(f),2)} 'c")
     

# How do you prevent a python print() function to print a new line at the end.
# print("a")
# print("b")
# print("c",end="")
# print("d",end="")



# Write a recursive function to calculate the sum of first n natural numbers.
# def sum(a):
#  if(a==1):
#   return 1
#  else:
#     return a+sum(a-1)
# a=int(input("enter the number : "))
# print(sum(a))



# Write a python function to print multiplication table of a given number.
# def mul(n):
#     i=1
#     while(i<=10):
#         print(i*n)
#         i+=1

# n=int(input("enter the number1 : ")) 
# mul(n)   



# Write a python function to print first n lines of the following pattern:
# ***
# ** - for n = 3
# *

def pattern(n):
    if(n==0):
        return
    print("*" *n)
    pattern(n-1)

pattern(5)  


# cms=inch*2.54

# Write a python function to remove a given word from a list ad strip it at the same
# time.

def rem(l,word):
    n=[]
    for item in l: 
         if not (item ==word):
             n.append(item.strip(word))
    return n
l=["monu","sonu","rohan","an"]
print(rem(l,"an"))