price_shirt = 25.00
price_jeans = 45.50

qty_shirt = 2
qty_jeans = 1

total_shirt = price_shirt * qty_shirt
total_jeans = price_jeans * qty_jeans
subtotal = total_shirt + total_jeans
print("Subtotal:", subtotal)

discount = subtotal * 0.10
print("Discount:", discount)

final_total = subtotal - discount
print("Final Total:", final_total)