def numbers(x: int) -> None:
  
    """
    Print digits of a natural number in reverse order, one per line.
    
    Parameters:
    x : int
        Natural number (positive integer)
        
    Returns:
    None
        The function only prints digits, doesn't return anything.
    """
  
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)
