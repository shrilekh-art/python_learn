# Python Challenges 🚀


# 2. Check if the password is at least 8 characters long and does not contain spaces
#    → len(password) >= 8 and " " not in password
pwd = "my_secure_password"

is_valid_pwd = len(pwd) >= 8 and " " not in pwd
print(is_valid_pwd)  # Output: True