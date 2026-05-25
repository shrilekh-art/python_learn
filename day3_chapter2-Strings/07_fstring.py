# ------------------- F-STRING NOTES -------------------
# f-string (formatted string):
# - Modern, super-easy way to format and build strings
# - "f" stands for "formatted"
# - Lets you embed variables and expressions directly inside a string
#
# Syntax:
# f"some text {variable_or_expression}"
#
# Example:
# name = "Shrilekh"
# age = 22
# print(f"My name is {name} and I am {age} years old.")
# → Output: My name is Shrilekh and I am 22 years old.
#
# Expressions also work:
# print(f"In 5 years, I will be {age + 5}.")
# → Output: In 5 years, I will be 27.
#
# Advantages:
# - Cleaner than .format() or % formatting
# - Readable and concise
# - Supports inline calculations and function calls
# ------------------------------------------------------
name = "Shrilekh"
age = 22
is_student = True
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")

print(f" 2+ 3 = {2+3}")