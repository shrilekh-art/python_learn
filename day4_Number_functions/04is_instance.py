# Type Validation: isinstance()

# isinstance(value, type)
# - Built-in function
# - Output: bool (True/False)
# - Checks if a value belongs to a certain data type

# Example:
x = 70
print(isinstance(x, int))   # True (x is an integer)

# More examples:
print(isinstance("hello", str))   # True
print(isinstance(3.14, float))    # True
print(isinstance([1,2,3], list))  # True
print(isinstance(70, float))      # False
