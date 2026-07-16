prices = [120, 250, 80, 450, 300, 150, 500, 220, 90, 400]

average_price = sum(prices) / len(prices)

above_average = [price for price in prices if price > average_price]

print("Average Price:", average_price)
print("Prices Above Average:", above_average)