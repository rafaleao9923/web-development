from typing import Dict, List, Set, Tuple

# interesting declaration of types
l: List[int] = [1, 2, 3, 4, 5]
t: Tuple[int, str, float] = (1, "hello", 3.14)
s: Set[int] = {1, 2, 3, 4, 5}
d: Dict[str, int] = {"a": 1, "b": 2, "c": 3}

print(l)  # [1, 2, 3, 4, 5]
print(t)  # (1, 'hello', 3.14)
print(s)  # {1, 2, 3, 4, 5}
print(d)  # {'a': 1, 'b': 2, 'c': 3}