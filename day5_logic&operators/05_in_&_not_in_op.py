# Membership operator examples  in and not in

# Check if a character is in a string
print("a" in "apple")        # True

# Check if an item is in a list
print(3 in [1, 2, 3, 4])     # True

# Check if a word is in a sentence
print("cat" in "The black cat sleeps")   # True

# Membership check with 'not in'

domain = "spam.com"
banned_domains = ["spam.com", "fake.org", "bot.net"]

# Check if domain is NOT in the banned list
print(domain not in banned_domains)   # False (because "spam.com" is banned)