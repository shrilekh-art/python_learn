import math

x = 1 
y = 1.1

print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(math.ceil(y))  # Output: 2
print(math.floor(y))  # Output: 1


price = 123.234232
print(round(price, 2))  # Output: 123.23

# Bankers Rounding (Round Half to Even)

# Rule:
# - When a number ends in .5 (a tie),
#   it is rounded to the nearest EVEN number.

# Examples:
# 2.5 → 2   (nearest even)
# 3.5 → 4   (nearest even)
# 4.5 → 4   (nearest even)
# 5.5 → 6   (nearest even)

# Purpose:
# - Avoids rounding bias in large datasets
# - Ensures balanced results over many calculations
n = 2.5
print(round(n))  # Output: 2
n2 = 3.5    
print(round(n2))  # Output: 4
