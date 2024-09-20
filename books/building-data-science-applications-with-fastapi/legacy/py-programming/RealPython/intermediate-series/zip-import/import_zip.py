import sys

# '''
# Insert the hello.zip into sys.path
sys.path.insert(0, "hello.zip")
print(sys.path[0])

# Import and use the code
import hello
hello.greet("Hung Pythonista")
# '''

'''
sys.path.append("goodbye_pkg.zip")
print(sys.path[-1])

from goodbye import greet
greet("Pythonista")
# '''
