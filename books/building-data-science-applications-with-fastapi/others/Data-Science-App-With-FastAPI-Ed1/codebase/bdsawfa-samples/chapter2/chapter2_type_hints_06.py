from typing import Tuple

# User defined type aliases
IntStringFloatTuple = Tuple[int, str, float]

# using user defined type alias
t: IntStringFloatTuple = (1, "hello", 3.14)

print(t)  # (1, 'hello', 3.14)