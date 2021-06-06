import math


def f12(x):
    if x < 60:
        return math.log(x - 74 * x ** 7 + 76) + 29 * x ** 6 + 34

    elif 60 <= x < 158:
        return 26 * x ** 5 - 40 * x ** 8

    elif 158 <= x < 191:
        return 28 * (math.log(x) + x ** 3) ** 5 + 44 * x

    elif 191 <= x < 282:
        return x ** 8 - x ** 4

    elif x >= 282:
        return x ** 8 - x ** 6
