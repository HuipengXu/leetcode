# @Time    : 2019/3/7 22:08
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

def isPalindrome0(s: str) -> bool:
    if len(s) in [0, 1]: return True
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True


def isPalindrome1(s: str) -> bool:
    if len(s) in [0, 1]: return True
    num_start = ord('0')
    capital_start = ord('A')
    lowercase_start = ord('a')

    def is_num_or_letter(c):
        if num_start <= ord(c) < num_start + 10:
            return True
        elif capital_start <= ord(c) < capital_start + 26:
            return True
        elif lowercase_start <= ord(c) < lowercase_start + 26:
            return True
        else:
            return False

    content = [c for c in s if is_num_or_letter(c)]
    if len(content) in [0, 1]: return True
    i, j = 0, len(content) - 1
    while i < j:
        if content[i].lower() != content[j].lower():
            return False
        i += 1
        j -= 1
    return True


if __name__ == "__main__":
    s = ",.pp"
    print(isPalindrome0(s))
