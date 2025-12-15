def pownum(a: float, n: int) -> float:
    """
      Calculate the power of a real number using recursion.

      Args:
          a (float): The base number - can be any real number
          n (int): The exponent - must be a natural number (0 or positive integer)

      Returns:
          float: The result of a raised to the power n (a^n)
    """
    if n == 0:
        return 1
    if n == 1:
        return a
    return a * pownum(a, n - 1)
