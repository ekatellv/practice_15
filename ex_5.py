def mod_number(a: int, b: int) -> int:
  
    """
    Recursively calculates the remainder of dividing natural number a by natural number b.
    
    Arguments:
    a : int
        The dividend (natural number to be divided)
    b : int
        The divisor (natural number to divide by)
        
    Returns:
    int: the remainder of a divided by b
    """
  
    if b == 0:
        raise ValueError('Cannot divide by zero')
    
    if a < b:
        return a
    
    return mod_number(a - b, b)
