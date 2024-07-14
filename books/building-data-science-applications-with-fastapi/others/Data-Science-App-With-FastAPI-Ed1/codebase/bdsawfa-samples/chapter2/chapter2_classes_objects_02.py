class Greetings:
    def __init__(self, default_name, age):
        self.default_name = default_name
        self.age = age

    def greet(self, name=None):
        return f"Hello, {name if name else self.default_name}"

    def get_age(self):
        return self.age

c = Greetings("Alan", 18)
print(c.default_name)  # "Alan"
print(c.greet())  # "Hello, Alan"
print(c.greet("John"))  # "Hello, John"
print(c.get_age())  # 18
