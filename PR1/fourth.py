import math

def f14(n):
    if n == 0:
        return 3
    elif n == 1:
        return 9
    else:
        return (1 / 80) * f14(n - 2) ** 2 + math.cos(f14(n - 2))
