def ten_to_n(x: int, n: int) -> str:

    """
    Convert a natural number from decimal to base-n system using recursion.
    
    Parameters:
    x : int
        Natural number (positive integer) in decimal system
    n : int
        Base to convert to (2 ≤ n ≤ 16)
        
    Returns:
    str
        Number representation in base-n system as a string
    """

    if not (2 <= n <= 16):
        raise ValueError("Base n must be between 2 and 16 inclusive")
    if x == 0:
        return "0"

    return _convert_to_base(x, n)


def _convert_to_base(x: int, n: int) -> str:
  
    """
    Helper recursive function to convert decimal to base-n.
    
    Parameters:
    x : int
        Positive integer to convert (x > 0)
    n : int
        Base to convert to (2 ≤ n ≤ 16)
        
    Returns:
    str
        Number representation in base-n as string
    """
  
    if x == 0:
        return ""
    
    remainder = x % n
    
    if remainder < 10:
        current_digit = str(remainder)
    else:
        current_digit = chr(ord('A') + remainder - 10)
    
    remaining_digits = _convert_to_base(x // n, n)
    return remaining_digits + current_digit


def _digit_to_char(digit: int) -> str:
  
    """
    Convert a digit (0-15) to its character representation.
    
    Parameters:
    digit : int
        Digit value (0-15)
        
    Returns:
    str
        Character representation
    """
  
    if 0 <= digit <= 9:
        return str(digit)
    elif 10 <= digit <= 15:
        # Convert 10→A, 11→B, ..., 15→F
        return chr(ord('A') + digit - 10)
    else:
        raise ValueError(f"Digit {digit} out of range 0-15")
