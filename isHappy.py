# @Time    : 2019/6/28 19:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            if n in visited: return False
            visited.add(n)
            tmp = []
            while n > 0:
                n, cur = divmod(n, 10)
                tmp.append(cur ** 2)
            n = sum(tmp)
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(45))
