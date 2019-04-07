# @Time    : 2019/4/7 15:23
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import Tuple


def calculate(s: str) -> int:
    def get_digits(i: int, step: int) -> Tuple[int, int]:
        e = i + step
        while e < len(s) and s[e].isdigit():
            e += 1
        return int(s[i + step - 1:e]), e

    stack = ['+']
    i = 0
    # 去掉空格
    s = ''.join([elem for elem in s if elem != ' '])
    while i < len(s):
        if s[i] == '*':
            num1 = int(stack.pop())
            num2, i = get_digits(i, 2)
            stack.append(num1 * num2)
        elif s[i] == '/':
            dividend = int(stack.pop())
            divisor, i = get_digits(i, 2)
            stack.append(dividend // divisor)
        elif s[i].isdigit():
            digits, i = get_digits(i, 1)
            stack.append(digits)
        else:
            stack.append(s[i])
            i += 1
    ret = j = 0
    while j < len(stack):
        if stack[j] == '+':
            ret += int(stack[j + 1])
        elif stack[j] == '-':
            ret -= int(stack[j + 1])
        j += 2
    return ret


def calculate1(s: str) -> int:
    # 为了将最后一部分计算完成
    s += '+0'
    stack, num, preOp = [], 0, "+"
    for i in range(len(s)):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif not s[i].isspace():
            if preOp == "-":
                stack.append(-num)
            elif preOp == "+":
                stack.append(num)
            elif preOp == "*":
                stack.append(stack.pop() * num)
            else:
                stack.append(stack.pop() // num)
            preOp, num = s[i], 0
    return sum(stack)


if __name__ == "__main__":
    s = " 100*2 + 1 / 1 * 12 / 7"
    print(calculate1(s))
