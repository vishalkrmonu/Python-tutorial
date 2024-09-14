#tuple never change
a=(2,)
print(type(a))


a=(2,3,5,6,8)
print(type(a))


a=(2,3,5,6,"vishal","rahul",8)
print(a)


# method
a=(2,3,5,6,"vishal","rahul",8)
print(a)
no=a.count(5)
print(no)


i=a.index(5)
print(i) 


a=(1,2,3)
repeated=a*3
print(repeated)

print(len(a))


# practice
# fruits=[]
# a=input("enter the element")
# fruits.append(a)
# b=input("enter the element")
# fruits.append(b)
# c=input("enter the element")
# fruits.append(c)
# d=input("enter the element")
# fruits.append(d)
# print(fruits)


# marks=[]
# a=int(input("enter the marks1 "))
# marks.append(a)
# b=int(input("enter the marks2 "))
# marks.append(b)
# c=int(input("enter the marks3 "))
# marks.append(c)
# d=int(input("enter the marks4 "))
# marks.append(d)
# marks.sort()
# print(marks)


# a=(34,45,"monu")
# a[2]="harry"  #cannot update tupple
# print(a)


l=[3,4,5,6]
print(sum(l))


l1=(3,2,1,5,5,5)
print("count of 5 is : ",l1.count(5))