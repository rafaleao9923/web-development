from collections import Counter

'''
multiset = Counter([1, 1, 2, 3, 3, 3, 4, 4])

temp = [1, 1, 2, 3, 3, 3, 4, 4]
print(temp)
print(set(temp))
print(multiset.keys())
'''

prices = {"course": 97.99, "book": 54.99, "wallpaper": 4.99}
cart = Counter(course=1, book=3, wallpaper=2)

# tmp_total = []
total = 0.0

for product, units in cart.items():
    subtotal = units * prices[product]
    price = prices[product]

    # tmp_total.append(subtotal)
    total += subtotal

    print(f"{product}: : ${price:7.2f} × {units} = {subtotal:.2f}")

# print(f"Total: {sum(tmp_total)}")
print(f"Total: {total}")
