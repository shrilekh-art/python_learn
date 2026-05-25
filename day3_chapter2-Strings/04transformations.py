#1 - replace
date = "2026-12-25"
print(date.replace("-", "/"))  # Output: 2026/12/25

price = "123,45"
print(price.replace(",","."))  # old value to be replaced with new value

phone = "123-456-7890"
print(phone.replace("-",""))  # Output: 1234567890

#chained methods are executed from left to right. So, the first replace() removes the "$" and the second replace() changes the commas to periods.
amount = "$122,22,22"
print(amount.replace("$","").replace(",",".")) # Output: 122.22.22