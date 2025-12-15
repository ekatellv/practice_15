def degree5(n: int) -> int:
  
    """
    Check if a number is a power of 5 and return the exponent.
    
    Parameters:
    n : int
        The natural number to check
        
    Returns:
    int
        - The exponent k if n = 5^k (where k ≥ 0)
        - -1 if n is not a power of 5
    """
  
    if n == 1:
        return 0
    elif n < 5 or n % 5 != 0:
        return -1
    else:
        result = degree5(n // 5)
        
        if result == -1:
            return -1
        else:
            return result + 1
