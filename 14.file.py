'''
 a="a very long string with emails"
 emails =[]
 3 seconds
 '''

# read
# f=open("file.txt")
# data=f.read()
# print(data)
# f.close()

# write
# st="my name is vishal"
# f=open("file1.txt","w")
# f.write(st)
# f.close()


# f=open("file.txt")
# lines=f.readlines()
# print(lines,type(lines))
# f.close()




# f=open("file.txt")
# line1=f.readline()
# print(line1,type(line1))

# line2=f.readline()
# print(line2,type(line2))

# line3=f.readline()
# print(line3,type(line3))

# line4=f.readline()
# print(line4,type(line4))

# line5=f.readline()
# print(line5=="")
# f.close()
 



f=open("file.txt")
line =f.readline()
while(line !=""):
    print(line)
    line=f.readline()
f.close()    



