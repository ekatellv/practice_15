def maxlist(a):
  
    """
    Find the maximum element in a list using recursion.
    
    Parameters:
    a : list
        List of integers (can be empty)
        
    Returns:
    int or None
        Maximum element in the list, or None for empty list
    """
  
    if not a:
        return None
    if len(a) == 1:
        return a[0]
  
    max_of_rest = maxlist(a[1:]) 
    return a[0] if a[0] > max_of_rest else max_of_rest
