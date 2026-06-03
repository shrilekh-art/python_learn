# Example: Classify a fruit order

fruit = "Mango"
quantity = 12
is_member = True

if fruit.lower() == "mango" and quantity >= 10:
    # Special bulk mango discount
    if is_member:
        print("Bulk mango discount + member bonus applied!")
    else:
        print("Bulk mango discount applied!")
elif fruit.lower() == "apple":
    print("Apple order processed.")
else:
    print("Regular order processed.")
