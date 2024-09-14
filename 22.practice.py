# Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class programmer:
    company="google"
    def __init__(self,name ,sal,pin): #constructor
        self.name=name
        self.sal=sal
        self.pin=pin 

p=programmer("monu",230000,34566)   
print(p.name,p.sal,p.pin,p.company) 

r=programmer("sonu",230000,34566)   
print(r.name,r.sal,r.pin,r.company)



# Write a class “Calculator” capable of finding square, cube and square root of a
# number.
class cal:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"square of anumber is : {self.n*self.n}")

    def cube(self):
        print(f"square of anumber is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"square of anumber is : {self.n**1/2}")        

a=cal(4) 
a.square()
a.cube()
a.squareroot()       



# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?
class demo:
    a=7

obj=demo() 
print(obj.a)   #print the class attribute because instance attribute is not present
obj.a=4         #instance attribute set
print(obj.a)    #print the instance attribute because instance aattribute is present
print(demo.a)     #print the class attribute



# Add a static method in problem 2, to greet the user with hello
class cal:
    def __init__(self,n):
        self.n=n

    def square(self):
        print(f"square of anumber is : {self.n*self.n}")

    def cube(self):
        print(f"square of anumber is : {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"square of anumber is : {self.n**1/2}")  
    @staticmethod
    def hello():
        print("hello")          

a=cal(4) 
a.square()
a.cube()
a.squareroot()    



# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint
class train:
    def __init__(self,trainNo):
        self.trainNo=trainNo

    def book(self,fro,to):
        print(f"ticketis booked in train no : {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f" train no :{self.trainNo} is running on time")

    def getfare(self,fro,to):
        print(f"ticketis fare in train no :{self.trainNo} from {fro} to {to} is {randint(222,5555)}")

t=train(11233)
t.book("rampur","delhi")
t.getstatus()
t.getfare("rampur","delhi")
