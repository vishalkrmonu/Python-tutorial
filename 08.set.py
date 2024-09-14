# set is collection of non-repeating element

s={2,4,5}

e=set() #dont use s={} as it will  create an empty dictionary

s={2,4,5,5,4,3,4}
print(s)

s={2,4,5,5,4,3,4,"vishal"}
s.add(566)
s.remove(2)
s.pop()
s.clear()
print(s,type(s))

# set method
# union & intersection
s1={1,2,4,5}
s2={3,5,7,1}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1-s2) 

# subsets
s1={1,2,4,5}
print(s1.issubset({1,2}))


# practice
# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
# words={
#     "madad":"help",
#   "raja":"king",
#   "kursi":"chairs"
# }
# word=input("enter the word : ")
# print(words[word])



# Write a program to input eight numbers from the user and display all the unique
# numbers (once).
# s=set()
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# a=int(input("enter the number1 : "))
# s.add(a)
# print(set)


# Can we have a set with 18 (int) and '18' (str) as a value in it?
s=set()
s.add(18)
s.add("18")
print(s)


# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique
dict={}
name=input("enter the name : ")
lang=input("enter the lang : ")
dict.update({name:lang})

name=input("enter the name : ")
lang=input("enter the lang : ")
dict.update({name:lang})

name=input("enter the name : ")
lang=input("enter the lang : ")
dict.update({name:lang})  #if key are  same  then it update only 
print(dict)


#in set we can not update any value if list is contain
# set can not contain list