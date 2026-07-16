def safe_division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both values must be numbers.")

print(safe_division(20, 5))
print(safe_division(20, 0))
print(safe_division(20, "5"))