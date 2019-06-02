# @Time    : 2019/6/2 19:00
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    # 超时
    def canWinNim(self, n: int) -> bool:
        memo = {}

        def recur(n: int) -> bool:
            if n <= 3: return True
            if n in memo: return memo[n]
            res = []
            for i in range(1, 4):
                tmp = not self.canWinNim(n - i)
                res.append(tmp)
                memo[n - i] = tmp
            memo[n] = any(res)
            return memo[n]

        return recur(n)

    def canWinNim1(self, n: int) -> bool:
        n %= 4
        n = 4 if n == 0 else n
        memo = {1: True, 2: True, 3: True}
        for i in range(4, n + 1):
            res = []
            for j in range(1, 4):
                if i - j <= 3:
                    memo[i] = True
                    break
                res.append(not memo[i - j])
            memo[i] = any(res)
        return memo[n]

    def canWinNim2(self, n: int) -> bool:
        return n % 4 != 0


if __name__ == '__main__':
    s = Solution()
    for i in range(18):
        print(s.canWinNim2(i))
