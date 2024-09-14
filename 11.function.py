# a=int(input("enter the number : "))
# b=int(input("enter the number: "))
# c=int(input("enter the number : "))
# avg=(a+b+c)/3
# print(avg)


# function
# def avg():   #function definition
#     a=int(input("enter the number: "))
#     b=int(input("enter the number: "))
#     c=int(input("enter the number : "))
#     avg=(a+b+c)/3
#     print(avg)
# avg()  #function call
# avg()    


def func1():
    print("hello")
func1()      



# function with argument
def func1(name):   #name is parameter
    print("hello "+name)
func1("monu") 


# function with argument
def func1(name,ending):   #name is parameter
    print("hello "+name)
    print(ending)
func1("monu","thanku") 
func1("sonu","thank you") 


# function with return
def func1(name,ending):   #name is parameter
    print("hello "+name)
    print(ending)
    return "ok"

a=func1("monu","thanku") 
print(a)


#default argument
def func1(name,ending="thanku"):   #name is parameter
    print(f"hello ,{name} ")
    print(ending)

func1("monu") 