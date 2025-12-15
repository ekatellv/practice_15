def progress(a1: float, r: float, n: int) -> float:
    """
    Recursively find the n-th term of an arithmetic progression.

    Args:
        a1 (float): The first term of the progression
        r (float): The common difference between terms
        n (int): The term number to find (1-based index)

    Returns:
        float: The n-th term of the arithmetic progression
    """
    if n == 1:
        return a1
    return r + progress(a1, r, n - 1)
