# @Time    : 2019/6/28 17:31
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def intToRoman(self, num: int) -> str:
        res, p = [], 1
        int_roman_map = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
                         40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD',
                         500: 'D', 900: 'CM', 1000: 'M'}
        while num > 0:
            num, cur = divmod(num, 10 ** p)
            num *= 10 ** p
            if cur in int_roman_map:
                res.append(int_roman_map[cur])
            elif 1 <= cur < 4:
                res.append(int_roman_map[1] * cur)
            elif 5 < cur < 9:
                res.append(int_roman_map[5] + int_roman_map[1] * (cur - 5))
            elif 10 < cur < 40:
                res.append(int_roman_map[10] * (cur // 10))
            elif 50 < cur < 90:
                res.append(int_roman_map[50] + int_roman_map[10] * ((cur - 50) // 10))
            elif 100 < cur < 400:
                res.append(int_roman_map[100] * (cur // 100))
            elif 500 < cur < 900:
                res.append(int_roman_map[500] + int_roman_map[100] * ((cur - 500) // 100))
            else:
                res.append(int_roman_map[1000] * (cur // 1000))
            p += 1
        return ''.join(res[i] for i in range(len(res) - 1, -1, -1))

    def intToRoman1(self, num: int) -> str:
        res = []
        int_roman_map = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        for int_, roman in int_roman_map.items():
            res.append(num // int_ * roman)
            num %= int_
        return ''.join(res)


if __name__ == '__main__':
    s = Solution()
    num = 2344
    print(s.intToRoman1(num))
