# @Time    : 2019/7/21 10:28
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

import re


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        nodes = preorder.split(',')
        i = 0
        while i < len(nodes):
            if len(stack) >= 2 and stack[-1] == stack[-2] == '#':
                stack = stack[:-3] + ['#']
            elif nodes[i] == '#' and len(stack) >= 2 and stack[-1] == '#':
                stack.pop()
                stack.pop()
                stack.append('#')
                i += 1
            else:
                stack.append(nodes[i])
                i += 1
        while len(stack) >= 3 and stack[-1] == stack[-2] == '#':
            stack = stack[:-3] + ['#']
        return len(stack) == 1 and stack[0] == '#'

    def isValidSerialization1(self, preorder: str) -> bool:
        stack = []
        nodes = preorder.split(',')
        i = 0
        while i < len(nodes) or len(stack) > 2:
            if len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3].isdigit():
                stack = stack[:-3] + ['#']
            else:
                stack.append(nodes[i])
                i += 1
        return len(stack) == 1 and stack[0] == '#'

    def isValidSerialization2(self, preorder: str) -> bool:
        pattern = re.compile(r'\d+,#,#')
        while pattern.search(preorder):
            preorder = pattern.sub('#', preorder)
        return preorder == '#'


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSerialization1("9,9,91,#,#,9,#,49,#,#,#"))
