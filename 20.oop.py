# class emp:
#     name="vishal"
#     language="eng"
#     sal=99999
# harry=emp()    #harry is obj
# print(harry.name,harry.language)    
  

# class emp:
#     language="eng" #class attribute
#     sal=99999
# harry=emp() 
# harry.name="visghal"   # obj instance attribute
# print(harry.name,harry.sal,harry.language) 




# instance vs class attribute
class emp:
    language="eng" #class attribute
    sal=99999
harry=emp() 
harry.language="math"   # obj instance attribute update kr dega class attribute ko
print(harry.sal,harry.language) 



# self parameter
class emp:
    language="eng" #class attribute
    sal=99999
    def getinfo(self):
        print(f"The language is  {self.language}. The salary is {self.sal}")

harry=emp()        
harry.language="javascript"  #this is an instance attribute
# harry.getinfo()
emp.getinfo(harry)




class emp:
    language="eng" #class attribute
    sal=99999
    def getinfo(self):
        print(f"The language is  {self.language}. The salary is {self.sal}")
    
    @staticmethod
    def greet():
        print("hello morning")

harry=emp()        
harry.language="javascript"  #this is an instance attribute
emp.getinfo(harry)
harry.greet()