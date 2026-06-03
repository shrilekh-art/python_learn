# Comparison Operators → return True or False

# Equal to
print(5 == 5)    # True

# Not Equal
print(5 != 3)    # True

# Less than
print(2 < 5)     # True

# Less than or Equal
print(5 <= 5)    # True

# Greater than
print(7 > 4)     # True

# Greater than or Equal
print(7 >= 7)    # True

# Comparison Operators with Expressions

# Equal to (==)
print(2 + 3 == 5)       # True (5 == 5)

# Not Equal (!=)
print(10 - 4 != 3)      # True (6 != 3)

# Less than (<)
print(7 / 2 < 4)        # True (3.5 < 4)

# Less than or Equal (<=)
print(2 - 1 <= 2)       # True (1 <= 2)

# Greater than (>)
print(3 * 3 > 8)        # True (9 > 8)

# Greater than or Equal (>=)
print(5 ** 2 >= 25)     # True (25 >= 25)


# Comparison Operators with Built-in Functions

# Equal to (==)
print(len("hi") == 3)        # False (len("hi") = 2, not 3)

# Not Equal (!=)
print(sum([1, 2, 3]) != 10)  # True (sum = 6, not 10)

# Less than (<)
print(max([2, 5, 7]) < 10)   # True (largest = 7, less than 10)

# Less than or Equal (<=)
print(len([1,2,3,4]) <= 5)   # True (length = 4, less than or equal to 5)

# Greater than (>)
print(min([4, 9, 2]) > 1)    # True (smallest = 2, greater than 1)

# Greater than or Equal (>=)
print(len("Python") >= 6)    # True (length = 6, equal to 6)

# Comparison Operators with Strings

# Equal to (==)
print("cat" == "cat")       # True (both strings are identical)

# Not Equal (!=)
print("dog" != "cat")       # True (different strings)

# Less than (<)
print("apple" < "banana")   # True ('a' comes before 'b')

# Less than or Equal (<=)
print("hi" <= "hi")         # True (equal strings)

# Greater than (>)
print("zebra" > "yak")      # True ('z' comes after 'y')

# Greater than or Equal (>=)
print("python" >= "java")   # True ('p' comes after 'j')

# Case-sensitive string comparisons

# Equal to (==)
print("Cat" == "cat")     # False (uppercase 'C' vs lowercase 'c')

# Not Equal (!=)
print("Dog" != "dog")     # True (different case makes them unequal)

# Greater than (>)
print("Zoo" > "apple")    # True ('Z' has higher Unicode value than 'a')


# Chained Comparisons - evalutions are from left to right, but all comparisons must be true for the whole expression to be true

# Numeric range check
x = 5
print(1 < x < 10)        # True (x is between 1 and 10)

# Multiple operators chained
y = 20
print(10 < y <= 20)      # True (y is greater than 10 AND less/equal to 20)

# With expressions
z = 15
print(10 < (z - 5) < 20) # True (10 < 10 < 20 → False, careful!)

# With strings (lexicographic order)
word = "cat"
print("ant" < word < "dog")  # True ('cat' is between 'ant' and 'dog')

# Chained Comparisons → like SQL's BETWEEN

age = 18

# Is age between 18 and 30?
print(18 <= age <= 30)   # True (age = 18, within bounds)

# Another example
age = 25
print(18 <= age <= 30)   # True (25 is between 18 and 30)

# Edge case
age = 31
print(18 <= age <= 30)   # False (31 is outside the range)

