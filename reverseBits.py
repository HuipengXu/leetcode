# @Time    : 2019/7/21 8:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = []
        while n > 0:
            n, remainder = divmod(n, 2)
            binary.append(remainder)
        binary += [0] * (32 - len(binary))
        p = len(binary) - 1
        ans = 0
        for bit in binary:
            ans += bit * 2 ** p
            p -= 1
        return ans

    def reverseBits1(self, n):
        res = 0
        for _ in range(32):
            res <<= 1
            res += n & 1
            n >>= 1
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(43261596))
