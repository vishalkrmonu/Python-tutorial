# never change the string


name="bishal"
a=name[0:4]  #index range
print(a)


char1=name[1]
print(char1)


name="bishal"
print(name[-4:-1])
print(name[1:4])

print(name[:4])  # is same as print(name[0:4])
print(name[1:])  # is same as print(name[1:5])
print(name[1:4])  


n="234567543"
print(n[1:6:2])


# string function
name="monu"
print(len(name))
print(name.endswith("u")) 
print(name.startswith("mo")) 
print(name.capitalize())
print(name.lower())
print(name.upper())


a="vishal is good boy"
print(a.replace("good" , "bad"))

a="vishal is good \n boy and \"real\"  \t world "
print(a)

# practice
name=input("enter your name ")
print(f"good afternnon {name}") #fstring


letter='''Dear <|Name|>,
 you are selected!
 <|Date|>'''
print(letter.replace("<|Name|>","monu").replace("<|Date|>" ,"24 sept 2025"))


#find the double space
a="vishal is good  boy"
print(a.find("  "))
print(a.find("goo"))



#convert double space to single space
a="vishal is good   boy"
print(a.replace("  "," "))
