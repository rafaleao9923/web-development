class A:
    def f(self):
        return "A"


class B:
    def f(self):
        return "B"

    def g(self):
        return f"B add {self.value}"


class C:
    def __init__(self, value) -> None:
        self.value = value


class Child(A, B, C):
    # why using A.f() instead of B.f()?
    pass


c = Child(10)
print(c.f())  # "A"
print(c.g())  # "B add 10"

# ------------------------- Mixins -------------------------
# Define a mixin class with some behavior


class JsonMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

# Create a base class that will use the mixin


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create a class that inherits from the base class and mixes in the JsonMixin


class JsonPerson(JsonMixin, Person):
    pass


# Create an instance of JsonPerson
person = JsonPerson("Alice", 30)

# Use the to_json method from the mixin
json_data = person.to_json()
print(json_data)  # Outputs: {"name": "Alice", "age": 30}
