
height_cm = "175"
weight_kg = "68.5"

height_int = int(height_cm)
weight_float = float(weight_kg)


height_m = height_int / 100
bmi = weight_float / (height_m * height_m)

print(f"Height in meters: {height_m}m")
print(f"Weight in kilograms: {weight_float}kg")
print(f"Calculated BMI: {round(bmi, 2)}")