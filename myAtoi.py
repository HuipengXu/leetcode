# @Time    : 2019/5/9 9:08
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if (len(s) == 0 or not (s[0].isdigit()
                                or s[0] == '+' or s[0] == '-')): return 0
        ret = []
        for i in range(len(s)):
            if (s[i] == '-' or s[i] == '+') and i == 0:
                ret.append(s[i])
            elif s[i].isdigit():
                ret.append(s[i])
            else:
                break
        num_str = ''.join(ret)
        if num_str == '+' or num_str == '-': return 0
        num = int(num_str)
        if num < -2 ** 31:
            return -2 ** 31
        elif num > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return num


if __name__ == '__main__':
    ss = "---89"
    s = Solution()
    print(s.myAtoi(ss))
