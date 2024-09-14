# a=int(input("enter your age: "))
# if(a>18):
#     print("you can  do vote")
# elif(a<0):
#     print("plaese enter valid number")    
# else:
#     print("you can not do vote")


# b=int(input("enter your age: "))
# if(b%2==0):
#     print("even number")
# if(b>=18):
#     print("you can  do vote")
# elif(b<0):
#     print("plaese enter valid number")    
# else:
    # print("you can not do vote")



# practice
# Write a program to find the greatest of four numbers entered by the user. 
# a=int(input("enter the number 1 : "))
# b=int(input("enter the number 2 : "))
# c=int(input("enter the number 3: "))
# d=int(input("enter the number 4 : "))
# if(a>b and a>c and a>d):
#     print("greatest number is a : ",a)
# elif(b>a and b>c and b>d):
#      print("greatest number is b : ",b)
# elif(c>a and c>b and c>d):
#      print("greatest number is b : ",b)
# else:
#     print("greatest number is d :", d)




# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user

# a=int(input("enter the marks 1 : "))
# b=int(input("enter the marks 2 : "))
# c=int(input("enter the marks 3: "))
# total_percent=(100*(a+b+c))/300
# if(total_percent >40 and a>33 and b>33 and c>33):
#     print("you are pass")
# else:
#     print("you are not pass")



# A spam comment is defined as a text containing following keywords:
# "Make a lot of money", "buy now", "subscribe this", "click this". Write a program
# to detect these spams.

# p1="Make a lot of money" 
# p2="buy now" 
# p3="subscribe this"
# p4="click this"
# message=input("enter your message: ")
# if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
#     print("this comment is a spam")
# else:
#     print("this is not spam")


# Write a program to find whether a given username contains less than 10
# characters or not.    
username=input("enter the text : ")
l=len(username)
if(l<20):
    print("it is not more than 20")
else:
    print("it is more than 20")



# Write a program which finds out whether a given name is present in a list or not  

l=["monu","sonu","tonu","ronu"]
name=input("enter the name : ")
if(name in l):
    print("your name is in the list")
else:
    print("your name is not in the list")



# Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F

mark=int(input("enter the marks : "))
if(mark>=90 and mark<=100):
    grade="Ex"
elif(mark<=90 and mark>=80) :
    grade="b"   
print(grade)    


# Write a program to find out whether a given post is talking about “Harry” or not
post=input("enter the text : ")
if("harry".lower() in post.lower() ):
    print("this is post is talking about harry")
else:
    print("this is not talking about harry")   