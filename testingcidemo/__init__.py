__version__ = "0.0.1"


def f(i):
    if not isinstance(i, int):
        raise TypeError("i must be an int")

    if i < 0 or i > 10:
        raise ValueError("i out of range")

    if i == 4:
        return "Apples"

    return i


def multi(x, y):
    return x*y
