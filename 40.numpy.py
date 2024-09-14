import numpy as np
list=[10,20,30,40,60]
arr=np.array(list)
print(arr)
print(type(arr))


list=[10,20.8,30,40,60]  #all value are convert in float
arr=np.array(list)
print(arr)

list=[10,'h',7.8,30,40,60]   #all convert in string
arr=np.array(list)
print(arr)


#2d array
list2=[[12,11,44],[34,23,43],[34,32,21]]
arr2=np.array(list2)
print(arr2)

arr3=np.arange(1,8)  #1 to 7 print
print(arr3)


arr3=np.arange(1,7).reshape((2,3))  #2-row,3-column
print(arr3)



arr3=np.zeros((4,3))  #1 to 7 print
print(arr3)


arr3=np.ones((4,3))  #1 to 7 print
print(arr3)
print("dimension : ",arr3.ndim)
print("shape  : ",arr3.shape)
print("size : ",arr3.size)



#attributes of numpy array
# ndim,shape,size,dtype,itemsize