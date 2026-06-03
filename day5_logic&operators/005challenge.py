# Python Challenges 🚀

# 5. Check if the user is either an admin or a moderator,
#    and either they’re not banned or they’ve verified their email
#    → (role in ["admin", "moderator"]) and (not banned or verified_email)

user_role = "admin"
banned = False
verified_email = True
is_valid_user = (user_role in ["admin", "moderator"]) and (not banned or verified_email)
print(is_valid_user)  # Output: True