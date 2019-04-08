# @Time    : 2019/4/8 10:48
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List, Union, Tuple


def evalRPN(tokens: List[str]) -> int:
    stack = []

    def get_nums(stack: List[int]) -> Tuple[int, int]:
        return int(stack.pop()), int(stack.pop())

    for elem in tokens:
        if elem.isdigit() or (elem.startswith('-') and len(elem) >= 2):
            stack.append(int(elem))
        elif elem == '+':
            num1, num2 = get_nums(stack)
            stack.append(num2 + num1)
        elif elem == '-':
            num1, num2 = get_nums(stack)
            stack.append(num2 - num1)
        elif elem == '*':
            num1, num2 = get_nums(stack)
            stack.append(num2 * num1)
        elif elem == '/':
            num1, num2 = get_nums(stack)
            stack.append(int(num2 / num1))
    return stack[0]


if __name__ == "__main__":
    tokens = ["4"]
    print(evalRPN(tokens))
