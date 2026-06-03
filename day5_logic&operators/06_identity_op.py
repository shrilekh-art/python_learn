# Make sure the email exists, and it's not empty.

email = None

# Condition explained:
# - email is not None → ensures the variable has been assigned something
# - email != ""      → ensures it's not just an empty string
# Combined with 'and', both checks must be True

print(email is not None and email != "")
# Output: False (since email = None)
