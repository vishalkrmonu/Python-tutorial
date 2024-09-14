# Write a program to find out whether a file is identical & matches the content of
# another file.
with open("this.txt") as f:
    content1=f.read()

with open("this_copy.txt") as f:
    content2=f.read() 

if(content1==content2):
    print("both are same")
else:
    print("both are not same")



# Write a program to wipe out the content of a file using python.
with open("this_copy.txt" ,"w") as f:
    f.write("") 
           



# Write a python program to rename a file to “renamed_by_ python.txt
with open("old.txt") as f:
    content1=f.read()

with open("rename.txt","w") as f:
    f.write(content1)    