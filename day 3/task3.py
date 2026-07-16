numbers = [15, 22, 15, 48, 60, 22, 75, 90, 48, 11, 60, 35, 90, 18, 35]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Unique Numbers:", unique_numbers)
