# ------------------- PYTHON CHALLENGE -------------------
# Task: Clean up a messy phone number format
#
# Example messy input:
# "+49 (176) 123-4567"
#
# Goal:
# - Convert into a clean format containing only digits
# - Expected output: "491761234567"

phone = "+49 (176) 123-4567"
print(phone.replace("+","").replace("(", "").replace(")", "").replace(" ", "").replace("-", ""  ))