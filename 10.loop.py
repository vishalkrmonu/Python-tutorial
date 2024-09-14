



# while
i=1
while(i<6):
    print(i)
    print("monu")
    i+=1     

# list using while loop  
l=[1,4,"monu",False,"rohan","sonu"]  
i=0
while(i<len(l)):
    print(l[i])
    i+=1

# for loop    
for i in range(4):
    print(i)
for i in range(0,100,4):
    print(i)    

# list  iteration   
l=[2,4,6,5,44,88,2]
for i in l:
    print(i)

# tuple  iteration   
t=(2,4,6,5,44,88,2)
for i in t:
    print(i)    

# string iteration   
s="harry"
for i in s:
    print(i) 

# for with else
l=[1,7,8]
for item in l:
    print(item)    
else:
    print("done")    

#  break   
for i in range(88):
    if(i==34):
        break #exit the loop right now
    print(i)

#continue  
for i in range(88):
    if(i==34):
        continue #skip the loop right now
    print(i)


# pass
l=[1,4,6]
for item in l:
    pass

i=0
while(i<45):
    print(i)
    i+=1


#practice  
# Write a program to print multiplication table of a given number using for loop.
# n=int(input("enter the digit : "))
# for i in range(1,11):
#     print(f"{n} x {i}={n*i}")
#     print(n*i)  


# Write a program to print multiplication table of a given number using for loop.
# n=int(input("enter the digit : "))
# for i in range(1,11):
#     print(f"{n} x {11-i}={n*(11-i)}")


# n=int(input("enter the digit : "))
# i=1
# while(i<11):
#     print(n*i)
#     i += 1



#  Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
l = ["Harry", "Soham", "Sachin", "Rahul"] 
for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")

# Write a program to find whether a given number is prime or not.
# n=int(input("enter the digit : "))
# for i in range(2,n):
#     if(n%i==0):
#       print("number is not prime") 
#       break
# else:   
#   print("number is prime")
     
        
# Write a program to find the sum of first n natural numbers using while loop
# n=int(input("enter the number : "))
# i=1
# s=0
# while(i<=n):
#     s=s+i
#     i+=1
# print(s)



# Write a program to calculate the factorial of a given number using for loop.
# num=int(input("enter the number : "))
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)     



# star pattern
# n=int(input("enter the number : "))
# for i in range(1,n+1):
#     print(" "* (n-i), end="")
#     print("*"* (2*i-1), end="")
#     print("")



# n=int(input("enter the number : "))
# for i in range(1,n+1):
#     print("*"* i, end="")
#     print("")




n=int(input("enter the number : "))
for i in range(1,n+1):
    if(i==1 or i==n):
        print("*"*n,end="")
    else:    
        print("*" ,end="")
        print(" "*(n-2) ,end="")
        print("*" ,end="")
    print("")    