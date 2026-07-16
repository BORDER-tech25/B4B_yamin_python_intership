def apply_discount(price, percent=10):
    discount = price * percent / 100
    final_price = price - discount
    return final_price

print("\n----- Discount -----")
print("Default Discount:", apply_discount(1000))
print("Custom Discount:", apply_discount(1000, percent=20))