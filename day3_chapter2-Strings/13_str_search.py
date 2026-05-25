# startswith() and endswith()
#find()
#in()

phone = "+1-202-555-0173"
print(phone.startswith("+1"))
print(phone.endswith("0173"))

email = "abc@gmail.com"
print(email.endswith("@gmail.com"))
print('@' in email)

file= "report.pdf"
print(file.endswith(".pdf"))

url = "https://www.example.com/index.html"
print('//' in url)

# find is always combined with other methods to add dynamism to our code
print(url.find("www"))  # Output: 8

