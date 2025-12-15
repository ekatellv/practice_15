def combin(n: int, k: int) -> int:

    """
    Calculate binomial coefficient C(n, k) using recursion.
    
    Parameters:
    n : int
        Total number of items (n >= 0)
    k : int
        Number of items to choose (0 <= k <= n)
        
    Returns:
    int
        Binomial coefficient C(n, k)
    """

    if k == 0 or k == n:
        return 1
    elif k > n or k < 0:
        return 0
    return combin(n - 1, k - 1) + combin(n - 1, k)
