from collections import Counter


def count_letters(filename):
    counter = Counter()
    with open(filename) as file:
        for line in file:
            line_letters = [char for char in line.lower() if char.isalpha()]
            counter.update(Counter(line_letters))
    return counter


letter_counter = count_letters("pyzen.txt")

for letter, count in letter_counter.most_common(3):
    print(letter, count)