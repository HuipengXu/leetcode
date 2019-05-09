from typing import List

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


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        i = 0
        flag = False
        while True:
            if i < len(strs[0]):
                tmp = strs[0][i]
            else:
                break
            for word in strs[1:]:
                if i < len(word) and word[i] == tmp:
                    continue
                flag = True
                break
            if flag:
                break
            else:
                i += 1
        return strs[0][:i]

    # 骚操作
    def longestCommonPrefix1(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        s1 = max(strs)
        s2 = min(strs)
        for i, c in enumerate(s2):
            if c != s1[i]:
                return s2[:i]
        return s2

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if len(strs) == 0: return ''
        common_prefix = strs[0]
        for s in strs[1:]:
            i = 0
            while i < len(common_prefix) and i < len(s):
                if s[i] == common_prefix[i]:
                    i += 1
                    continue
                break
            if common_prefix == '': return ''
            common_prefix = common_prefix[:i]
        return common_prefix


if __name__ == '__main__':
    ss = ["flower", "flow", "flight"]
    s = Solution()
    print(s.longestCommonPrefix1(ss))
    print(s.longestCommonPrefix2(ss))
