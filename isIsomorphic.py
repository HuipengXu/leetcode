# @Time    : 2019/7/17 11:06
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        transform, visited = {}, set()
        for cs, ct in zip(s, t):
            if cs in transform:
                if transform[cs] == ct: continue
                return False
            else:
                if ct in visited: return False
                transform[cs] = ct
                visited.add(ct)
        return True

    def isIsomorphic1(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        transform = {}
        for cs, ct in zip(s, t):
            if cs in transform:
                if transform[cs] == ct: continue
                return False
            else:
                if ct in transform.values(): return False
                transform[cs] = ct
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        return [*map(s.index, s)] == [*map(t.index, t)]


if __name__ == '__main__':
    s = Solution()
    print(s.isIsomorphic('bar', 'foo'))
