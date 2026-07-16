class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")
        self._celsius = value

    @property
    def kelvin(self):
        return self._celsius + 273.15


temp = Temperature(25)

print("Celsius:", temp.celsius)
print("Kelvin:", temp.kelvin)

try:
    temp.celsius = -300
except ValueError as e:
    print(e)