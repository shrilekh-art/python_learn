# any() function → returns True if at least one element is truthy

email = ""
phone = ""
username = ""

# Allows registration if ANY field is filled
print(any([email, phone, username]))   # False (all empty)

# If at least one is non-empty → True
# Example:
email = "abc@example.com"
print(any([email, phone, username]))   # True


# all() function → returns True only if EVERY element is truthy

first_name = "Shrilekh"
last_name = "Patil"
age = "27"

# Registration allowed only if ALL fields are filled
print(all([first_name, last_name, age]))   # True

# Example with one empty field
first_name = ""
last_name = "Patil"
age = "27"
print(all([first_name, last_name, age]))   # False


# Type Checking: isinstance()
print(isinstance(123, int))    # True (123 is an integer)
print(isinstance(True, str))   # False (True is not a string)

# String Methods: endswith() / startswith()
print("Hello".endswith("o"))   # True (string ends with 'o')
print("Hello".startswith("o")) # False (string does not start with 'o')
