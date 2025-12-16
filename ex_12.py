def search(a: list, x: int) -> int:
    
    """
    Search for an integer x in a list a using recursion.

    Parameters:
    a : list
        List of integers to search in
    x : int
        Integer to search for

    Returns:
    int
        1 if x is found in the list, 0 otherwise
    """

    if not a:
        return 0
    if a[0] == x:
        return 1

    return search(a[1:], x)
