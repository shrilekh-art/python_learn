# Python Challenges 🚀

# 4. Check if a username is a string, is not None, and is longer than 5 characters
#    → isinstance(username, str) and username is not None and len(username) > 5

uname = "Alice"

is_valid_user = isinstance(uname , str) and uname is not None and len(uname) > 5
print(is_valid_user)  # Output: False
