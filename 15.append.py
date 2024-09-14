# st="hey vishal you are too good"
# f=open("file.txt","a")
# f.write(st)
# f.close()


# f=open("file.txt")
# print(f.read())
# f.close()

#the same can be written using with statement like this :
# with open("file.txt") as f: #we can direct using
#     print(f.read())


# practice    
f=open("poem.txt")
content=f.read()
if("twinkle" in content):
    print("the word is present")
else:
    print("the word is not present")
f.close()