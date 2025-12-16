def ten_to_bin(x: int) -> str:
  
    """
    Convert a natural number from decimal to binary using recursion.
    
    Parameters:
    x : int
        Natural number (positive integer) in decimal system
        
    Returns:
    str
        Binary representation of the number as a string
    """

    if x == 0:
        return "0"
    return _convert_to_binary(x)


def _convert_to_binary(x: int) -> str:
  
    """
    Helper recursive function to convert decimal to binary.
    
    Parameters:
    x : int
        Positive integer to convert (x > 0)
        
    Returns:
    str
        Binary representation as string
    """

    if x == 0:
        return ""
    
    current_digit = str(x % 2)
    remaining_binary = _convert_to_binary(x // 2)

    return remaining_binary + current_digit
