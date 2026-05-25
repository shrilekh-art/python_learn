# split() 
# - Splits a string into a list of substrings based on a specified delimiter.
sentence = "Hello world, welcome to Python programming!"
words = sentence.split()  # Default delimiter is any whitespace
print(words)  # Output: ['Hello', 'world,', 'welcome', 'to', 'Python', 'programming!']

stamp = "2024-06-25 18:30:00"
print(stamp.split())  # Output: ['2024-06-25', '18:30:00']

date = "2026-12-25"
print(date.split("-"))  # Output: ['2026', '12', '25']

csv_file = "1234,John Doe,USA"
print(csv_file.split(","))  # Output: ['1234', 'John Doe', 'USA']