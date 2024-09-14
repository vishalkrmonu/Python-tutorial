def myFunc():
    print("hello world ")



if __name__ == "__main__":
    print("we are directly running this code")
    myFunc()
    print(__name__)  


# global variable
# a=78
# def fun():
#     a=8
#     print(a)

# print(a)
# fun()   


a=78
def fun():
    global a
    a=8
    print(a)
    
fun() 
print(a)


# enumerate function
# list1 = [1,7,12,11,22,]
# index=0
# for i in list1:
#     print(f"the item  number at index  {index } is {i} ")
#     index +=1



# this can be simplified using enumerate function
list1 = [1,7,12,11,22,]
for index ,i in enumerate(list1):
    print(f"the item  number at index  {index } is {i} ")
    



#    LIST COMPREHENSIONS
list1 = [1,7,12,11,22,]
# squareList=[]
# for item in list1:
#     squareList.append(item*item)

squareList=[i*i for i in list1]
print(squareList)    