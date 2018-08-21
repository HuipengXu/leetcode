def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    min_word = min(strs, key=len)
    index = 0
    for i in range(1, len(min_word)+1):
        prefix = [s[:i] for s in strs]
        if len(set(prefix)) == 1:
            index += 1
        else:
            break
    return strs[0][:index]

