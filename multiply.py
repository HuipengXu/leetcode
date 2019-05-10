# @Time    : 2019/5/10 14:14
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ret = []
        for i in range(len(num1)):
            for j in range(len(num2)):
                multiplier = 10 ** i * int(num1[len(num1) - i - 1])
                multiplicand = 10 ** j * int(num2[len(num2) - j - 1])
                ret.append(multiplier * multiplicand)
        return str(sum(ret))

    def multiply1(self, num1: str, num2: str) -> str:
        def str2num(num: str) -> int:
            ret = 0
            for i in range(len(num)):
                ret = ret * 10 + ord(num[i]) - ord('0')
            return ret

        n1 = str2num(num1)
        n2 = str2num(num2)
        return str(n1 * n2)

    # 参考：https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation
    def multiply2(self, num1: str, num2: str) -> str:
        l1, l2 = len(num1), len(num2)
        pos = [0] * (l1 + l2)
        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1
                sum_ = pos[p2] + mul
                pos[p2] = sum_ % 10
                pos[p1] += sum_ // 10
        ret = ''.join(map(str, pos))
        return ret.lstrip('0')


if __name__ == '__main__':
    s = Solution()
    num1 = "123"
    num2 = "456"
    print(s.multiply(num1, num2))
    print(s.multiply1(num1, num2))
    print(s.multiply2(num1, num2))
