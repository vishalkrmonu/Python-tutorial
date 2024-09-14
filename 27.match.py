def http_status(status):
    match status:
       case 200:
          return "OK"
       case 404:
          return "Not Found"
       case 500:
          return "Internal Server Error"
       case _:
          return "Unknown status"
# Usage
print(http_status(200)) # Output: OK
print(http_status(404)) # Output: Not Found
print(http_status(500)) # Output: Internal Server Error
print(http_status(403)) # Output: Unknown status



# merge dictionary
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged) 


with (open('file1.txt') as f1,
open('file2.txt') as f2
    
):
   #process file