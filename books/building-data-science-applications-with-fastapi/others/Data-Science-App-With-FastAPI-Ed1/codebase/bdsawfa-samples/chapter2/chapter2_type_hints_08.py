from typing import Callable, List

# generic class that expects two things: list of arguments and return type
ConditionFunction = Callable[[int], bool]


def filter_list(l: List[int], condition: ConditionFunction) -> List[int]:
    return [i for i in l if condition(i)]


def is_even(i: int) -> bool:
    # this is_even function is satisfed the ConditionFunction type
    return i % 2 == 0

# def is_odd(i: int) -> str:
#     # not satified the ConditionFunction type???
#     return "odd" if i % 2 != 0 else "even"

def is_odd(i: int) -> bool:
    return i % 2 != 0

temp = filter_list([1, 2, 3, 4, 5], is_even)
print(temp)  # [2, 4]

temp2 = filter_list([1, 2, 3, 4, 5], is_odd)
print(temp2)