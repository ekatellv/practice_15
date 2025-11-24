def sum_progress(a1: float, r: float, n: int) -> float:
    """
    Recursively find the sum of first n terms of an arithmetic progression.

    Args:
        a1 (float): The first term of the progression
        r (float): The common difference between terms
        n (int): The number of terms to sum

    Returns:
        float: The sum of first n terms of the arithmetic progression
    """
    if n == 1:
        return a1
    else:
        return (a1 + (n - 1) * r) + sum_progress(a1, r, n - 1)
