# import pkg.mod1, pkg.mod2

# from pkg import mod1, mod2

# pkg.mod1.foo()

# import pkg

# pkg.mod1

# print(pkg.A)

# mod1.foo()

# import pkg

# pkg.mod1.foo()

# from pkg import *   # import all

# print(dir())

# mod2.bar()
# mod4.qux()

# print(dir(mod1))

# mod1.foo()
# mod1.foo_bar()

from pkg.mod1 import *  # import all from mod1

print(dir())
foo()
foo_bar()