# @Time    : 2019/3/2 16:07
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


def superEggDrop(K: int, N: int) -> int:
    memo = {}

    def dp(k, n):
        if (k, n) not in memo:
            if k == 1:
                ans = n
            elif n == 0:
                ans = 0
            else:
                low, high = 1, n
                while low + 1 < high:
                    x = low + ((high - low) >> 1)
                    t1 = dp(k - 1, x - 1)
                    t2 = dp(k, n - x)
                    if t1 < t2:
                        low = x
                    elif t1 > t2:
                        high = x
                    else:
                        low = high = x
                ans = min(max(dp(k - 1, x - 1), dp(k, n - x)) for x in (low, high)) + 1
            memo[(k, n)] = ans
        return memo[(k, n)]

    return dp(K, N)
