def function1(x: int) -> int:
  
    """
    Check if a natural number is prime using recursion.
    
    Parameters:
    x : int
        Natural number to check (x > 0)
        
    Returns:
    int
        1 if the number is prime, 0 otherwise
    """

    if x <= 1:
        return 0  
    if x == 2:
        return 1 

    return _is_prime_recursive(x, 2)


def _is_prime_recursive(x: int, divisor: int) -> int:
  
    """
    Helper recursive function to check primality.
    
    Parameters:
    x : int
        Number to check
    divisor : int
        Current divisor to test
        
    Returns:
    int
        1 if prime, 0 if not prime
    """

    if divisor * divisor > x:
        return 1
    if x % divisor == 0:
        return 0
    
    return _is_prime_recursive(x, divisor + 1)
