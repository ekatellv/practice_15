def count(n: int) -> int:
    """
    Recursively count the number of digits in a natural number.

    Args:
        n (int): A natural number (non-negative integer)

    Returns:
        int: The number of digits in the given number
    """
    if n < 10:
        return 1
    else:
        return 1 + count(n // 10)
