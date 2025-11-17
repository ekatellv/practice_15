def progress(a1: float, r: float, n: int) -> float:
    if n == 1:
        return a1
    else:
        return r + progress(a1, r, n - 1)
