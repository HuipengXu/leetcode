# @Time    : 2019/5/30 7:52
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = '' if numerator ^ denominator >= 0 else '-'
        res = [sign]
        numerator, denominator = abs(numerator), abs(denominator)
        quotient, remainder = divmod(numerator, denominator)
        if remainder == 0: return sign + str(quotient)
        res.append(str(quotient) + '.')
        numerator = remainder * 10
        remainder_map = {}
        while numerator % denominator != 0:
            quotient, remainder = divmod(numerator, denominator)
            if (quotient, remainder) in remainder_map:
                break
            remainder_map[(quotient, remainder)] = len(res)
            res.append(str(quotient))
            numerator = remainder * 10
        if numerator % denominator == 0:
            res.append(str(numerator // denominator))
            return ''.join(res)
        else:
            repeat = '(' + ''.join(res[remainder_map[(quotient, remainder)]:]) + ')'
            prefix = ''.join(res[:remainder_map[(quotient, remainder)]])
            return prefix + repeat


if __name__ == '__main__':
    s = Solution()
    print(s.fractionToDecimal(-50, 8))
