# import sys
# import mod

import importlib
import mod2

# import re

# from mod import *
# from os import path

# print(mod.__file__)

# print(__file__)

# parent = path.abspath(__file__ + "/../")
# print(parent)

# sys.path.append(parent)
# print(sys.path)

# print(re.__file__)

# print(mod)

# foo(parent)

# print(dir())    # show all properties of the current module

# mod2.foo('quux')

print(mod2.a)

importlib.reload(mod2)

print(mod2.a)
