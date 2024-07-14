# subtracts
from collections import Counter

inventory = Counter(apple=39, orange=30, banana=15)
print(inventory)

wastage = Counter(apple=2, orange=15, banana=4) # use Counter
inventory.subtract(wastage)
print(inventory)

order_1 = {"apple": 12, "orange": 12}   # use dict
inventory.subtract(order_1)
print(inventory)

# use iterable
order_2 = ["apple", "apple", "apple", "apple", "banana", "banana"]
inventory.subtract(order_1)
print(inventory)

print(wastage + Counter(order_2))
print(Counter(order_1) + Counter(order_2))