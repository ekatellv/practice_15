def nod(a: int, b: int) -> int:
  
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using Euclid's algorithm.
    
    Parameters:
    -----------
    a : int
        First integer
    b : int
        Second integer
        
    Returns:
    --------
    int
        The greatest common divisor of a and b
    """
  
    if b == 0:
        return a
    return nod(b, a % b)
