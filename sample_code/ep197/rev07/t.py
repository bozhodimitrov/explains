import builtins

x = 1  # global scope


def print(*args, **kwargs):
    builtins.print('intercepted!')
    builtins.print(*args, **kwargs)


def f():

    y = 2  # closure scoped
    z = 4

    def g():

        z = 3  # local scope

        l_func = lambda z: z ** 2

        print(l_func(5))

        print(x, y, z)  # relative to here

    return g


g_func = f()

g_func()
