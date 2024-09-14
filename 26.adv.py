# WALRUS OPERATOR
# Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
 print(f"List is too long ({n} elements, expected <= 3)")



# TYPES DEFINITIONS IN PYTHON
n:int =5
name:str="harry"


def sum(a:int,b:int) ->int:
  return a+b


# Variable type hint
age: int = 25
# Function type hints
def greeting(name: str) -> str:
   return f"Hello, {name}!"
# Usage
print(greeting("Alice")) # Output: Hello, Alice!



# ADVANCED TYPE HINTS
from typing import List, Tuple, Dict, Union
# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
# Tuple of a string and an integer
person: Tuple[str, int] = ("Alice", 30)
# Dictionary with string keys and integer values
scores: Dict[str, int] = {"Alice": 90, "Bob": 85}
# Union type for variables that can hold multiple types
identifier: Union[int, str] = "ID123"
identifier = 12345 # Also valid