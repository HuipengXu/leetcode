# @Time    : 2019/6/5 8:01
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    # 回溯超时
    def numDecodings(self, s: str) -> int:
        res = 0

        def back_tracking(s: str) -> None:
            nonlocal res
            if not s:
                res += 1
                return
            if int(s[:1]) > 0: back_tracking(s[1:])
            if len(s) > 1 and not s[:2].startswith('0') and 0 < int(s[:2]) <= 26:
                back_tracking(s[2:])

        back_tracking(s)
        return res

    # dp
    def numDecodings1(self, s: str) -> int:
        if not s or s.startswith('0'): return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i] += dp[i - 1]
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                tmp = dp[i - 2] if i - 2 >= 0 else 1
                dp[i] += tmp
        return dp[-1]

    def numDecodings2(self, s: str) -> int:
        if not s or s.startswith('0'): return 0
        pre_pre = pre = 1
        for i in range(1, len(s)):
            cur = 0
            if s[i] != '0':
                cur += pre
            if s[i - 1] != '0' and int(s[i - 1:i + 1]) <= 26:
                cur += pre_pre
            pre_pre, pre = pre, cur
        return pre


if __name__ == '__main__':
    s = Solution()
    ss = "123456132541353454254315426342156"
    print(s.numDecodings(ss))
    print(s.numDecodings1(ss))
    print(s.numDecodings2(ss))
