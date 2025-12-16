def ind_maxlist(a, index=0):
    """
    Find the index of the maximum element in a list using recursion.

    Parameters:
    a : list
        List of integers (can be empty)

    Returns:
    int or None
        Index of the maximum element in the list, or None for empty list.
        If there are multiple maximums, returns the first occurrence.
    """

    if not a:
        return None
    if len(a) == 1:
        return 0

    max_index_in_rest_slice = ind_maxlist(a[1:])
    max_index_in_rest = max_index_in_rest_slice + 1

    if a[0] >= a[max_index_in_rest]:
        return 0
    else:
        return max_index_in_rest 
