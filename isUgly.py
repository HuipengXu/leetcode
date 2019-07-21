# @Time    : 2019/7/21 9:40
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        while num > 1:
            for divider in [2, 3, 5]:
                tmp, remainder = divmod(num, divider)
                if remainder == 0:
                    num = tmp
                    break
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(6))
