class Counter:
    def __init__(self):
        self.counter = 0

    def __call__(self, inc=1):
        self.counter += inc


c = Counter()
print(c.counter)  # 0
c()
print(c.counter)  # 1
# c(10)
c(2)
print(c.counter)  # 11