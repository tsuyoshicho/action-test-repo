def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def div(a: int, b: int) -> int:
    if b != 0:
        return a // b
    else:
        return 0
