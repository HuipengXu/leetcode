# @Time    : 2019/5/12 9:09
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def factorial(n: int) -> list:
            ret = [0] * n
            f = 1
            for i in range(1, n + 1):
                f *= i
                ret[i - 1] = f
            return ret

        ret = []
        nums = [i for i in range(1, n + 1)]
        factorials = factorial(n)
        n -= 1
        while k > 1:
            n_factorial = factorials[n - 1]
            num = (k - 1) // n_factorial
            ret.append(str(nums[num]))
            del nums[num]  # 比 nums.pop(num) 快很多
            k -= n_factorial * num
            n -= 1
        for num in nums:
            ret.append(str(num))
        return ''.join(ret)

    def getPermutation1(self, n: int, k: int) -> str:
        permutation = []
        nums = list(range(1, n + 1))
        k -= 1
        while n > 0:
            n -= 1
            index, k = divmod(k, math.factorial(n))
            permutation.append(str(nums[index]))
            del nums[index]
        return ''.join(permutation)


if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(8, 560))
    print(s.getPermutation1(8, 560))
