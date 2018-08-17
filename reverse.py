def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x >= 0:
        reverse_x = int(str(x)[::-1])
    else:
        reverse_x = - int(str(abs(x))[::-1])
    if reverse_x > 2 ** 31 - 1 or reverse_x < -2 ** 31:
        return 0
    return reverse_x
