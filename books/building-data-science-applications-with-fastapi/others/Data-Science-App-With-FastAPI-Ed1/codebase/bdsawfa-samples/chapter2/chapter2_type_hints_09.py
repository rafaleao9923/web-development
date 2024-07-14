from typing import Any


def f(x: Any) -> Any:
    # it's can be anything
    return x


value = f("a")
print(value)

value = f(10)
print(value)

value = f([1, 2, 3])
print(value)