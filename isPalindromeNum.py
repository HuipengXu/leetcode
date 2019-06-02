# @Time    : 2019/6/2 8:42
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_str = str(x)
        i, j = 0, len(num_str) - 1
        while i < j:
            if num_str[i] == num_str[j]:
                i += 1
                j -= 1
                continue
            return False
        return True

    def isPalindrome1(self, x: int) -> bool:
        if x < 0: return False
        res = []
        while x >= 1:
            tmp = x // 10
            res.append(x - tmp * 10)
            x = tmp
        i, j = 0, len(res) - 1
        while i < j:
            if res[i] == res[j]:
                i += 1
                j -= 1
                continue
            return False
        return True

    def isPalindrome2(self, x: int) -> bool:
        if x < 0: return False
        div = 1
        while x // div >= 10: div *= 10
        while x > 0:
            left = x // div
            right = x % 10
            if left != right: return False
            x = (x % div) // 10
            div //= 100
        return True

    def isPalindrome3(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0): return False
        revert_num = 0
        while revert_num < x:
            num = x % 10
            revert_num = revert_num * 10 + num
            x //= 10
        return revert_num == x or revert_num // 10 == x


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome3(121))
