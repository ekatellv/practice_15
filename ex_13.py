def odd_list(a: list[int], n: int) -> list[int]:

    """
    Return a list containing only even numbers from the input list.

    Parameters:
    a : list
        List of integers
    n : int
        Number of elements to process (typically len(a), but can be less)

    Returns:
    list[int]
        List containing only even numbers from the first n elements of a
    """

    if n == 0:
        return []

    even_numbers_in_rest = odd_list(a, n - 1)
    current_element = a[n - 1]

    if current_element % 2 == 0:
        return even_numbers_in_rest + [current_element]
    else:
        return even_numbers_in_rest
