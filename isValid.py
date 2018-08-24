def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    l_pth = [0]
    parathesis = {')':'(', ']':'[', '}':'{'}
    for pth in s:
        if pth in parathesis and parathesis[pth] == l_pth[-1]:
            l_pth.pop()
        else:
            l_pth.append(pth)
    return len(l_pth) == 1
