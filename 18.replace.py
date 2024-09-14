# word ="donkey"
# with open("file2.txt") as f:
#     content=f.read() 

# contentNew=content.replace(word,"####") 
# with open("file2.txt", "w") as f:
#     f.write(contentNew)
      

# words =["donkey","bad","ganda"]
# with open("file2.txt") as f:
#     content=f.read()  

# for word in words:
#  content=content.replace(word,"#" *len(word)) 

# with open("file2.txt", "w") as f:
#     f.write(content)


# Write a program to mine a log file and find out whether it contains ‘python’.
# with open("log.txt") as f:
#     content=f.read()
# if("python" in content):
#     print("python is  present")
# else:
#     print("python is not present")



# Write a program to find out the line number where python is present from ques 6.
# with open("log.txt") as f:
#     lines=f.readlines()

# lineno=1
# for line in lines:
#     if("python" in line):
#        print(f"python is  present line num: {lineno}")
#        break
#     lineno+=1    
# else:
#     print("python is not present")





# Write a program to make a copy of a text file “this. txt”
with open("this.txt") as f:
   content =f.read()

with open("this_copy.txt", "w") as f:
    f.write(content)    