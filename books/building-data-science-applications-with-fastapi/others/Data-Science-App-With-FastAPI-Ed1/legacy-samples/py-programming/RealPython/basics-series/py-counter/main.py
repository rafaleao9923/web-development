from collections import defaultdict, Counter

'''
word = "mississippi"
counter = defaultdict(int)
for letter in word:
    counter[letter] += 1

# print(counter)

# print(Counter(word))
# print(Counter(list(word)))

temp = Counter(i=4, s=4, p=2, m=1)
print(temp)

# tmp = Counter({"i": 4, "s": 4, "p": 2, "m": 1})
# print(tmp)

# print(Counter(set("mississippi")))

inventory = Counter(
    apple=10,
    orange=15,
    banana=0,
    tomato=-15
)


temp.update("missouri")
print(temp)

# tmp_2 = Counter({"i": "4", "s": "4", "p": "2", "m": "1"}) # not oke
tmp_2 = Counter({"i": 4, "s": 4, "p": 2, "m": 1})   # oke
tmp_2.update('missouri')
print(tmp_2)

'''
sales = Counter(apple=10, orange=15, banana=20, tomato=25)
print(sales)
monday_sales = Counter(apple=10, orange=8, banana=3)    # use COunter (as k, v pair)
sales.update(monday_sales)
print(sales)

tuesday_sales = {"apple": 4, "orange": 7, "tomato": 4}  # use dict
sales.update(tuesday_sales)
print(sales)

# most common objects
print(sales.most_common(2))

# least common objects
print(sales.most_common()[:-2 - 1:-1])