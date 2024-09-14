d={} #empty dictionary
marks={
    "Harry":100,
    "vishal":56,
    "rohan":23
}
print(marks,type(marks))

print(marks["Harry"])

# method
marks1={
    "Harry":100,
    "vishal":56, 
    "rohan":23,
    0:"monu"
}
print(marks1.items())
print(marks1.keys())
print(marks1.values())
marks1.update({"Harry":99})
marks1.update({"Harry":99,"mona":20})

print(marks1)



print(marks.get("harry2"))   #prints None
print(marks["harry2"])       #returns an error