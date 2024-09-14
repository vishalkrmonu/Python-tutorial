# class emp:
#     language="eng" #class attribute
#     sal=99999
#     def getinfo(self):
#         print(f"The language is  {self.language}. The salary is {self.sal}")
    
#     def __init__(self):  #dunder method auto called
#         print("i am creating an object")

#     @staticmethod
#     def greet():
#         print("hello morning")

# harry=emp()        
# harry.name="monu"  
# print(harry.name,harry.sal)




class emp:
    language="eng" #class attribute
    sal=99999
    def getinfo(self):
        print(f"The language is  {self.language}. The salary is {self.sal}")
    
    def __init__(self,name,sal,language):  #dunder method auto called
        self.name=name
        self.sal=sal
        self.language=language
        print("i am creating an object")


    @staticmethod
    def greet():
        print("hello morning")

harry=emp("vishal",66666,"py")        
harry.name="monu"  
print(harry.name,harry.sal,harry.language)