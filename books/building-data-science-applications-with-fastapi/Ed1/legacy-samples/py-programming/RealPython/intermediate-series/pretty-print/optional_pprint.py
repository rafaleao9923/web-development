from urllib import request
from pprint import pprint, PrettyPrinter, pformat

# response = request.urlopen("https://jsonplaceholder.typicode.com/users")
# json_response = response.read()

import json

# users = json.loads(json_response)

# with open('users.json', 'w') as f:
#     json.dump(users, f)

with open('users.json') as f:
    users = json.load(f)
# print(*users)

# for user in users:
#     print(user)

# -------------------------- depth --------------------------
# pprint(users)
# pprint(users, depth=2)
# pprint(users[0], depth=1)

# -------------------------- indent --------------------------
# pprint(users[0], depth=1, indent=2)

# pprint(users[0], depth=2, indent=2)

# -------------------------- width --------------------------
# pprint(users[0], width=160)
# pprint(users[0], width=5)

# -------------------------- compact --------------------------
# pprint(users, depth=1, width=40, compact=True)
# pprint(users[0], depth=1, width=20, compact=True)


# -------------------------- stream --------------------------
'''
with open('users.txt', mode="w") as f:
    pprint(users, stream=f)
    # pprint(users, depth=2, width=5, stream=f)
    # pprint(users, depth=2, width=25, stream=f)
# '''
# -------------------------- sort_dicts: 3.8 --------------------------
# pprint(users[0], depth=1, sort_dicts=False)


# -------------------------- underscore_numbers: 3.10 --------------------------
number_list = [123456789, 10000000000000]
# pprint(number_list, underscore_numbers=True)


# -------------------------- Custom PrettyPrinter --------------------------
custom_printer = PrettyPrinter(
    indent=4,
    width=100,
    depth=2,
    compact=True
)

# custom_printer.pprint(users[0])

# -------------------------- pformat --------------------------
address = pformat(users[0]["address"])
chars_to_remove = ["{", "}", "'"]
for char in chars_to_remove:
    # print(char)
    # print("--------------")
    address = address.replace(char, "")
# print(address)

# -------------------------- Handling Recursive --------------------------
A = {}
B = {"link": A}
A["link"] = B
print(A)
pprint(A)
'''
print(B)
pprint(B)
# '''
