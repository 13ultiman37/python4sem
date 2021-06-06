def f22(x1):
    x = x1
    A = x & (2 ** 16 - 1)
    x >>= 16
    B = x & (2 ** 8 - 1)
    x >>= 8
    C = x & (2 ** 6 - 1)
    x >>= 6
    D = x & (2 ** 2 - 1)
    return D | C << 18 | A << 2 | B << 24


print(hex(f22(0xfaf9be9e)))
