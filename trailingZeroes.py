def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """
    import math
    n_power = math.floor(math.log(n, 5))
    n_number = [n // int(math.pow(5, i)) for i in range(1, n_power+1)]
    return sum(n_number)