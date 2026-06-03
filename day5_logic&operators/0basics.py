# Control Flow

# Definition:
# - Control Flow is the logic you write to control how your code runs.

# Key questions:
# - Should I run this part of the code?
# - Should I skip it?
# - Should I repeat it?

# Control Flow is implemented using:
# - Conditionals (if / elif / else)
# - Loops (for / while)
# - Function calls and returns

# Control Flow + Boolean Expressions

# Control Flow Statements:
# - Conditional: if, elif, else
# - Loops: for, while
# - Loop Control: break, continue, pass

# Boolean Expressions:
# Values:
#   True, False
# Functions:
#   bool(), any(), all(), isinstance()
# Comparison Operators:
#   ==, !=, <, >, >=, <=
# Logical Operators:
#   and, or, not
# Membership Operators:
#   in, not in
# Identity Operators:
#   is, is not

# Example combining both:
x = 10
y = [1, 2, 3]

if isinstance(x, int) and x > 5:
    print("x is an integer greater than 5")

for i in y:
    if i == 2:
        continue   # skip 2
    print(i)

# Output:
# x is an integer greater than 5
# 1
# 3
