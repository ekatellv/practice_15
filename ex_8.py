def fib(k: int) -> int:
  
    """
    Calculate the k-th Fibonacci number using recursion.
    
    The Fibonacci sequence is defined as:
    F(0) = 0
    F(1) = 1
    F(n) = F(n-1) + F(n-2) for n >= 2
    
    Parameters:
    k : int
        The index of the Fibonacci number to calculate (non-negative integer)
        
    Returns:
    int
        The k-th Fibonacci number
    """
    if k == 0:
        return 0
    elif k == 1:
        return 1
    return fib(k - 1) + fib(k - 2)
