import math


def f11(x, y, z):
    return math.log1p(y - (74 * z ** 7) + 76) + 29 * y ** 5 + 34 + 26 * y ** 6 - 40 * z ** 5 - math.sqrt(
        (28 * y ** 5 + x) / (44 * x * x + 59 * x ** 7))
