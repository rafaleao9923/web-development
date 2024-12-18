kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# print(kirk, spock, mccoy)


# class Dog:
#     def __init__(self):
#         print("This is a Dog")
#     pass


class Dog:
    species = "Canis familiaris"    # class attribute

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} barks {sound}"

# a = Dog()
# b = Dog()

# print(a == b)


# buddy = Dog_Info("Buddy", 5, "Golden Retriever")
# miles = Dog_Info("Miles", 12, "Corgi")

# print(buddy.age, miles.age)

# miles.age = 10
# print(buddy.age)

# print(miles)
# print(miles.speak("Howl"))


class BullDog(Dog):
    def __init__(self, name, age, breed, color):    # if have new atrribute
        super().__init__(name, age, breed)
        self.color = color

    def __str__(self):
        return f"{self.name} is {self.age} years old {self.color} {__class__.__name__}"


class Dachshund(Dog):
    def __init__(self, name, age, breed, personality):  # if have new atrribute
        super().__init__(name, age, breed)
        self.personality = personality

    def __str__(self):
        return f"{self.name} is {self.age} years old {self.personality} {__class__.__name__}"


class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"


dashChild = Dachshund("Dash", 5, "Dachshund", "Loud")
print(dashChild)

bullChild = BullDog("Bull", 7, "Bulldog", "Brown")
print(bullChild)

print(isinstance(dashChild, BullDog))

miles = JackRussellTerrier("Miles", 4, "Jack Russell Terrier")
print(miles.speak("Woof"))

homelander = GoldenRetriever("HomeLander", 6, "Golden Retriever")
print(homelander.speak())
