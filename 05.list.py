#string are not mutable but list are mutable

friend=["apple","banana",5,34.5,"monu"]
print(friend[2])

friend[0]="grapes" #list are mutalbe
print(friend[0 ])
print(friend[1:3])


friend=["apple","banana",5,34.5,"monu","vishal"]
print(friend)
friend.append("harry") #append means at the end add krna 
print(friend)



l1=[1,3,4,55,34,2,1,66]
l1.sort()
print(l1)
l1.reverse()
print(l1)


l1=[1,3,4,55,34,2,1,66]
l1.insert(3,2222)    #index,value
print(l1)

l1=[1,3,4,55,34,2,1,66]
l1.pop(3)    #delete at index 3
print(l1)


l1=[1,3,4,55,34,2,1,66]
l1.remove(3)    #delete at value
print(l1)