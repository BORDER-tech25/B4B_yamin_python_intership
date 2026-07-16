def create_counter(start):
    value = start

    def counter():
        nonlocal value
        value += 1
        return value

    return counter

counter1 = create_counter(0)
counter2 = create_counter(100)

print(counter1())
print(counter1())
print(counter1())

print(counter2())
print(counter2())