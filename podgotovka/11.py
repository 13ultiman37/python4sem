import math


def f11(x):
    return (x ** 4 + math.sin(x) / x ** 6 + 23 * x ** 5 + 6) + math.cos(47 * x ** 7 - x ** 8 - 50) - math.tan(
        x) + 34 * x ** 7 + 45 * x ** 6


def f12(x):
    if x < 54:
        return x ** 5 - x ** 7
    elif 54 <= x < 120:
        return x ** 6 + 23 * x ** 5 + 6
    elif x >= 120:
        return math.cos(47 * x ** 7 - x ** 8 - 50) - math.tan(x) + 14


def f13(n, m):
    x = 0
    y = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x += i ** 4 + math.sin(i)
    for i in range(1, n + 1):
        y += 94 * i - 74 * i ** 8 - 29

    return 39 * x + 66 * y


def f14(n):
    if n == 0:
        return 4
    else:
        return math.cos(f14(n - 1) + (1 / 50) * f14(n - 1) ** 2)


def f21(x):
    if x[0] == 'frege':
        if x[2] == 'stan':
            if x[1] == 'xs':
                return 0
            elif x[1] == 'llvm':
                return 1
        elif x[2] == 'metal':
            return 2
        elif x[2] == 'perl6':
            if x[1] == 'xs':
                return 3
            elif x[1] == 'llvm':
                return 4
    elif x[0] == 'ston':
        return 5
    elif x[0] == 'gap':
        if x[2] == 'stan':
            return 6
        elif x[2] == 'metal':
            if x[1] == 'xs':
                return 7
            elif x[1] == 'llvm':
                return 8
        elif x[2] == 'perl6':
            if x[3] == 2008:
                return 9
            elif x[3] == 1994:
                return 10
            elif x[3] == 1961:
                return 11


def f22(n):
    x = n
    A = x & (2 ** 2 - 1)
    x >>= 2
    B = x & (2 ** 8 - 1)
    x >>= 8
    C = x & (2 ** 15 - 1)
    x >>= 15
    D = x & (2 ** 7 - 1)

    return B | A << 8 | D << 10 | C << 17


class C32:
    def __init__(self):
        self.state = 'A'
        self.states = {
            'A': {
                'slur': ('B', 0)
            },
            'B': {
                'sway': ('C', 1)
            },
            'C': {
                'slur': ('D', 2),
                'sway': ('E', 3)
            },
            'D': {
                'crush': ('A', 5),
                'slur': ('F', 6)
            },
            'E': {
                'sway': ('F', 7),
                'slur': ('A', 8)
            }
        }

    def set_state(self, method):
        try:
            new_state = self.states.get(self.state).get(method)
            if new_state is None:
                raise RuntimeError
            self.state = new_state[0]
            return new_state[1]
        except RuntimeError:
            return None

    def slur(self):
        return self.set_state('slur')

    def sway(self):
        return self.set_state('sway')

    def crush(self):
        return self.set_state('crush')


o = C32()
print(o.slur())
print(o.sway())
print(o.slur())
print(o.slur())