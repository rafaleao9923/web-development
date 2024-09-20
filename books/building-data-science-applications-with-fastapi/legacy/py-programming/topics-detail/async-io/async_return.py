async def g():
    # Pause here and come back to g() when f() is ready
    r = await f()
    return r


async def f(x):
    y = await z(x)  # OK - `await` and `return` allowed in coroutines
    return y

async def f2(x):
    return await z(x)  # OK - `await` and `return` allowed in coroutines

async def g(x):
    yield x  # OK - this is an async generator


async def m(x):
    yield from gen(x)  # No - SyntaxError
    pass


def m(x):
    y = await z(x)  # Still no - SyntaxError (no `async def` here)
    return y
    pass
