class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


print(Car('blue', '20,000'))
print(Car('red', '30,000'))