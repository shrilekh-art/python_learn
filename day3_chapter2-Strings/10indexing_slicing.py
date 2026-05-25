# string - sequence of characters
# "hello" is a string
# Each character in the string has a position number (index)
# Indexing starts at 0
# Positive indices:
# h → 0
# e → 1
# l → 2
# l → 3
# o → 4

# Negative indices:
# h → -5
# e → -4
# l → -3
# l → -2
# o → -1

str = "Hello"
print(str[0])  # Output: H
print(str[-3])  # Output: l

# String Slicing in Python

# General form: [start:end]
# - Start index is INCLUDED
# - End index is NOT INCLUDED

# Positive indices: 0  1  2  3  4
# Characters:       h  e  l  l  o
# Negative indices: -5 -4 -3 -2 -1

# Example:
# word[0:3] → "hel"
# (includes index 0,1,2 but excludes 3)

# Another example:
# word[1:4] → "ell"
# (includes index 1,2,3 but excludes 4)

str2 = "Programming"
print(str2[0:8])

# open ended slicing
print(str2[0:])  # Output: Programming
print(str2[:8])  # Output: Program

# step slicing
print(str2[0:8:2])  # Output: Porm
print(str2[::3])  # Output: Pgg

date = "2024-06-25"
# extract year 
print(date[0:4])  # Output: 2024
# extract month
print(date[5:7])  # Output: 06
# extract day   
print(date[8:10])  # Output: 25

print(date[0:4],date[5:7],date[8:10])  # Output: 2024 06 25