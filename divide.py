# @Time    : 2019/5/26 20:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    # 超时
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend >= 0 and divisor >= 0 or
                dividend < 0 and divisor < 0):
            sign = '+'
        else:
            sign = '-'
        dividend = abs(dividend)
        divisor = abs(divisor)
        if divisor == 1:
            quotient = dividend
        elif divisor == dividend:
            quotient = 1
        elif divisor > dividend:
            return 0
        else:
            quotient = -1
            for i in range(0, dividend, divisor):
                quotient += 1
        quotient = quotient if sign == '+' else -quotient
        if quotient > 2 ** 31 - 1: return 2 ** 31 - 1
        if quotient < -2 ** 31: return -2 ** 31
        return quotient

    def divide1(self, dividend: int, divisor: int) -> int:
        res = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        divd = abs(dividend)
        dior = abs(divisor)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2 ** 31, res), 2 ** 31 - 1)


if __name__ == '__main__':
    dividend = 10
    divisor = -3
    s = Solution()
    print(s.divide(dividend, divisor))
    print(s.divide1(dividend, divisor))
