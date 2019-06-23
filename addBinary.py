# @Time    : 2019/6/23 8:34
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 and j >= 0:
            if a[i] == '1' and b[j] == '1':
                if carry == 0:
                    res.append('0')
                else:
                    res.append('1')
                carry = 1
            elif a[i] == '0' and b[j] == '0':
                if carry == 0:
                    res.append('0')
                else:
                    res.append('1')
                    carry = 0
            else:
                if carry == 1:
                    res.append('0')
                else:
                    res.append('1')
            i -= 1
            j -= 1
        if i == -1:
            while j >= 0:
                if b[j] == '1':
                    if carry == 0:
                        res.append('1')
                    else:
                        res.append('0')
                else:
                    if carry == 0:
                        res.append('0')
                    else:
                        res.append('1')
                        carry = 0
                j -= 1
        else:
            while i >= 0:
                if a[i] == '1':
                    if carry == 0:
                        res.append('1')
                    else:
                        res.append('0')
                else:
                    if carry == 0:
                        res.append('0')
                    else:
                        res.append('1')
                        carry = 0
                i -= 1
        if carry: res.append(str(carry))
        return ''.join(res[::-1])

    def addBinary1(self, a: str, b: str) -> str:
        res, carry = [], 0
        if len(a) > len(b):
            b = '0' * (len(a) - len(b)) + b
        elif len(a) < len(b):
            a = '0' * (len(b) - len(a)) + a
        i = max(len(a), len(b)) - 1
        while i >= 0:
            if a[i] == '1' and b[i] == '1':
                if carry == 0:
                    res.append('0')
                else:
                    res.append('1')
                carry = 1
            elif a[i] == '0' and b[i] == '0':
                if carry == 0:
                    res.append('0')
                else:
                    res.append('1')
                    carry = 0
            else:
                if carry == 1:
                    res.append('0')
                else:
                    res.append('1')
            i -= 1
        if carry: res.append(str(carry))
        return ''.join(res[::-1])


if __name__ == '__main__':
    s = Solution()
    print(s.addBinary('11', '1'))
    print(s.addBinary1('11', '1'))
