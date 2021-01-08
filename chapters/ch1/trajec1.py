from more_itertools import iterate, take


def f(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n  + 1


print(take(20, iterate(f, 56)))
print(take(2**8, iterate(f, 998123456789)))

