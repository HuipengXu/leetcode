# 累加数
def isAdditiveNumber(num):
     """
     :type num: str
     :rtype: bool
     """
    if (num == None or len(num) < 3):
        return False
    for i in range(1, len(num) // 2 + 1):
        if num[0] == '0' and i > 1:
            break
        s1 = num[0: i]
        num1 = int(s1)
        print(num1)
        for j in range(i + 1, len(num) - i + 1):
            if num[i] == '0' and j > i + 1:
                break
            s2 = num[i: j]
            num2 = int(s2)
            if (restIsAdditiveNumber(num[j:], num1, num2)):
                return True
    return False


def restIsAdditiveNumber(num, num1, num2):
    if len(num) == 0:
        return True
    add = num1 + num2
    add_s = str(add)
    return num.startswith(add_s) and restIsAdditiveNumber(num[len(add_s):], num2, add)


