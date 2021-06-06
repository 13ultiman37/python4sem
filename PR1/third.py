import math


def f13(n, m):
    x = 0;
    y = 0;
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            x += math.log(i) + math.fabs(i) + 55
    for i in range(1, n + 1):
        y += i ** 3 + i ** 7
    return 83 * x - y
