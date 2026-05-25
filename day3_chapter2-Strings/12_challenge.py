# Python Challenge: Clean the string

# Messy string:
# "968-Maria, ( D@t@ Engineer );; 27y.."

# Goal: Turn into a clean summary
# Desired output:
# name: maria | role: data engineer | age: 27

str = "968-Maria, ( D@t@ Engineer );; 27y.."

noice = str.strip("968-, (  );; , .y")
print(noice)  # Output: "Maria, ( D@t@ Engineer ) 27"