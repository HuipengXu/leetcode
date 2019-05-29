# @Time    : 2019/5/29 20:24
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    # 无法获得小数位
    def myPow(self, x: float, n: int) -> float:
        cnt_decimal = len(str(x).split('.')[-1])
        x = 1 / x if n < 0 else x
        n = abs(n)
        tmp, m = 1, x
        res = []
        while tmp <= n:
            pre = m
            m *= m
            tmp <<= 1
            if tmp >= n:
                num = m if tmp == n else pre
                n -= tmp >> 1
                tmp = 1
                res.append(num)
                m = x
        p = 1
        for num in res:
            p *= num
        p = round(p, cnt_decimal)
        return min(max(-2 ** 31, p), 2 ** 31 - 1)

    def myPow1(self, x: float, n: int) -> float:
        if n < 0: return self.myPow1(1 / x, -n)
        if x == 1 or n == 0: return 1
        if n % 2:
            return x * self.myPow1(x * x, n // 2)
        else:
            return self.myPow1(x * x, n // 2)

    def myPow2(self, x: float, n: int) -> float:
        if x == 1 or n == 0: return 1
        if n < 0:
            x, n = 1 / x, -n
        res = 1
        while n > 0:
            if n % 2:
                res *= x
                n -= 1
            else:
                x *= x
                n //= 2
        return res


if __name__ == '__main__':
    x = 2.10000
    n = 3
    s = Solution()
    print(s.myPow(x, n))
    print(s.myPow1(x, n))
