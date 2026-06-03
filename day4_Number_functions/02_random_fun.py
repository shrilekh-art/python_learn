import random 


# Random Number Generation in Python

# random.random()
# - Returns a random float between 0.0 and 1.0
# - Output type: float

# Example:
# import random
# value = random.random()
# print(value)   # e.g., 0.374829...
print(random.random())

# Random Integer Generation in Python

# randint(start, end)
# - Returns a random whole number (integer)
# - Range includes both start and end

# Example:
# import random
# value = random.randint(1, 6)
# print(value)   # e.g., 3 (any number between 1 and 6)
print(random.randint(1, 6))

# Tip: Use random functions to generate test data (dummy values)
# Examples: age, ID numbers, prices

# Example with randint():
# import random
# age = random.randint(18, 60)       # random age between 18 and 60
# user_id = random.randint(1000, 9999)  # random 4-digit ID
# price = random.randint(50, 500)    # random price between 50 and 500

# These are useful for testing programs without real data.
