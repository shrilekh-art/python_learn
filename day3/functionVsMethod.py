# ------------------- NOTES -------------------
# Function vs Method in Python
#
# Function:
# - Defined using 'def' keyword outside of a class.
# - Called independently: function_name(args).
# - Example: len([1,2,3]), print("Hello").
#
# Method:
# - A function that belongs to an object/class.
# - Invoked on an instance: object.method(args).
# - Example: list.append(4), str.upper().
#
# Key Difference:
# - Functions stand alone.
# - Methods are tied to objects and often modify or
#   interact with that object’s internal state.
# ---------------------------------------------
 
txt = 'hi'
num = 10

print(txt.upper())  # Method: upper() is a method of the string object 'txt'
print(len(txt))     # Function: len() is a standalone function that takes 'txt'

