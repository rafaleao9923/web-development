def even_numbers(max):
    for i in range(2, max + 1):
        if i % 2 == 0:
            yield i
    # code after the last yield statement is well executed
    print("Generator exhausted")


even = list(even_numbers(10))
print(even)