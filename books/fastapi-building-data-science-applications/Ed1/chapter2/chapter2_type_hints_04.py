from typing import Union


def greeting(name: Union[str, None] = None) -> str:
    # Optional[str] = None ~ Union[str, None] = None
    return f"Hello, {name if name else 'Anonymous'}"


print(greeting())  # "Hello, Anonymous"
print(greeting("Alice"))  # "Hello, Alice"