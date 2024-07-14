import pathlib
from collections import Counter


entries = pathlib.Path("./").iterdir()
# print(list(entries))
extensions = [entry.suffix for entry in entries if entry.is_file()]
# print(extensions)
print(Counter(extensions))
print(Counter(extensions).most_common(1))