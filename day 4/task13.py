def get_value(data, index):
    try:
        return data[index]
    except IndexError:
        return None

numbers = [10, 20, 30]

print(get_value(numbers, 1))
print(get_value(numbers, 5))