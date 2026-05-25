# ------------------- PYTHON DATA TYPES -------------------
# Organized into 3 broad categories:
#
# 1. No Value:
#    - NoneType → None
#
# 2. Single Value:
#    - Numeric:
#        * int → 15
#        * float → 3.15
#        * complex → 3 + 5j
#    - str → 'Hello'
#    - bool → True, False
#    - Date & Time:
#        * date → 2026-12-25
#        * time → 18:05:30
#        * datetime → 2026-12-25 18:05:30
#
# 3. Multi-Values:
#    - list → [1, 2, 3]
#    - tuple → (1, 2, 3)
#    - set → {1, 2, 3}
#    - dict → {'a': 1, 'b': 2}
#    - array → array('i', [10, 20])
#
# Quick Tip:
# - Use single value types for atomic data.
# - Use multi-value types for collections.
# ---------------------------------------------------------
# ------------------- PYTHON CHALLENGE -------------------
# Create 5 variables, each with a different data type:
#
# 1. Your age            → int
#    Example: age = 21
#
# 2. Your height         → float (decimal)
#    Example: height = 5.9
#
# 3. Your name           → str (string)
#    Example: name = "Shrilekh"
#
# 4. Are you a student?  → bool (True/False)
#    Example: is_student = True
#
# 5. Something with no value yet → NoneType
#    Example: future_plan = None
#
# Tip:
# - int, float, str, bool, NoneType are all single-value data types.
# - This exercise helps practice assigning values of different types.
# ---------------------------------------------------------

age = 29
height = 5.5
name = "Shrilekh"
is_student = True
future_plan = None

print(age, height, name, is_student, future_plan)
print(type(age), type(height), type(name), type(is_student), type(future_plan))
print(len(name))  

#day 1 to 3 for intro to python data types, functions, methods, and standard library. -> chapter 1 of python programming for beginners.
