def qux():
    print('[mod4] qux()')


class Qux:
    pass


from .. import sub_pkg_1
sub_pkg_1.mod1.foo()
# print()

from ..sub_pkg_1.mod1 import foo
foo()