def pownum(a: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n == 1:
        return a
    else:
        return a * pownum(a, n - 1)
