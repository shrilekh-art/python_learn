# Float Validation: is_integer()

# is_integer() → checks if a float value represents a whole number

# Example 1:
x = 7.0
print(x.is_integer())   # True (7.0 is an integer value)

# Example 2:
y = 7.1
print(y.is_integer())   # False (7.1 is not a whole number)

# More examples:
# 40.00.is_integer()     → True
# 25.00.is_integer()     → True
# 36554.000.is_integer() → True
