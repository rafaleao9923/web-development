from collections import Counter
import pathlib


def mode(data):
    counter = Counter(data)
    # print(counter.most_common(1)[0])
    _, top_count = counter.most_common(1)[0]
    return [point for point, count in counter.items() if count == top_count]


print(mode([2, 1, 2, 2, 3, 5, 3]))
print(mode([2, 1, 2, 2, 3, 5, 3, 3]))


data = [
    "apple",
    "orange",
    "apple",
    "apple",
    "orange",
    "banana",
    "banana",
    "banana",
    "apple",
]
print(mode(data))

print(mode(Counter(apple=4, orange=4, banana=2)))