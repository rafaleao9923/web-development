class A:
    def f(self):
        return "A"


class Child(A):
    # just using parent class method
    pass


c = Child()
print(c.f())  # "A"