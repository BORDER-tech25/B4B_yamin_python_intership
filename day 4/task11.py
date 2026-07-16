def make_validator(min_value):

    def validate(number):
        return number >= min_value

    return validate

validator10 = make_validator(10)
validator50 = make_validator(50)

print(validator10(5))
print(validator10(15))

print(validator50(30))
print(validator50(70))