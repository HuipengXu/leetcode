# @Time    : 2019/5/17 9:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    # 自顶向下，超时
    def climbStairs(self, n: int) -> int:
        memo = {}

        def recur(n: int) -> int:
            if n <= 2: return n
            if n in memo: return memo[n]
            paths = self.climbStairs(n - 1) + self.climbStairs(n - 2)
            memo[n] = paths
            return paths

        return recur(n)

    def climbStairs1(self, n: int) -> int:
        if n <= 2: return n
        memo = {}
        memo[1], memo[2] = 1, 2
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        return memo[n]

    def climbStairs2(self, n: int) -> int:
        if n <= 2: return n
        pre_pre, pre = 1, 2
        cur = 3
        for i in range(3, n + 1):
            cur = pre + pre_pre
            pre, pre_pre = cur, pre
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(35))
    print(s.climbStairs1(35))
