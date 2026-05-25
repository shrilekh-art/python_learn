#Math
password = 'abc123'
print(len(password))  # Output: 6

if len(password)<8 or len(password)>13:
    print("Password not valid")

# ------------------- STRING MATH NOTES -------------------
# Example: Working with multiline strings
#
text = """
Python is easy to learn.
Python is powerful.
Many people love python.
"""
#
# String Method: count(substring)
# - Belongs to the str class
# - Output type: int
# - Returns how often a word/substring appears in the string
# - Case-sensitive: 'Python' and 'python' are different
# Example:
print(text.count("Python")) 
print(text.count("love"))   

#can be used for data quality checks also ex no $
print(text.count("$"))  # Output: 0 (no $ in the text)

# Tip:
# Use count() for quick text analysis, like word frequency.
# ---------------------------------------------------------
