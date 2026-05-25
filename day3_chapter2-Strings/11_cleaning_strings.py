# String Cleaning Methods

# Clean Whitespaces:
#   lstrip()  → removes leading spaces
#   rstrip()  → removes trailing spaces
#   strip()   → removes spaces from both ends

# Clean Cases:
#   lower()   → converts all characters to lowercase
#   upper()   → converts all characters to uppercase

name = "   John Doe   "
print(name.lstrip())  # Output: "John Doe   "
print(name.rstrip())  # Output: "   John Doe"
print(name.strip())   # Output: "John Doe"

text = "###ABC###"
print(text.strip("#"))  # Output: "ABC"

sentence = " Hi there! , Welcome to Python programming. "
print(sentence.strip(" ,."))  # Output: "Hi there! , Welcome to Python programming"

txt = "  Engineering"
print(len(txt))  # Output: 14
print(len(txt.strip()))  # Output: 11

#cases
txt2 = "Python Programming"
print(txt2.lower())  # Output: "python programming"

txt3 = "Data Science"
print(txt3.upper())  # Output: "DATA SCIENCE"

search = "Python"
data = "pytHon"

print(search == data)  # Output: False
print(search.lower().strip() == data.lower().strip())  # Output: True