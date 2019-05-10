# @Time    : 2019/5/10 19:52
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ret = []
        ip = []

        def back_tracking(i: int) -> None:
            if (len(s) - i > 3 and len(ip) >= 3) or (i < len(s) and len(ip) >= 4): return
            if i == len(s) and len(ip) == 4:
                ret.append('.'.join(ip))
                return
            for j in range(1, 4):
                sub_s = s[i: i + j]
                if (len(sub_s) == 0 or int(sub_s) > 255
                        or (len(sub_s) >= 2 and sub_s.startswith('0'))):
                    continue
                ip.append(sub_s)
                back_tracking(i + j)
                ip.pop()

        back_tracking(0)
        return ret

    def restoreIpAddresses1(self, s: str) -> List[str]:
        ret = []
        for i in range(1, 4):
            for j in range(1, 4):
                for m in range(1, 4):
                    for n in range(1, 4):
                        if (i + j + m + n) != len(s):
                            continue
                        s1 = s[:i]
                        if (len(s1) >= 2 and s1.startswith('0')) or int(s1) > 255: continue
                        s2 = s[i: i + j]
                        if (len(s2) >= 2 and s2.startswith('0')) or int(s2) > 255: continue
                        s3 = s[i + j: i + j + m]
                        if (len(s3) >= 2 and s3.startswith('0')) or int(s3) > 255: continue
                        s4 = s[i + j + m: i + j + m + n]
                        if (len(s4) >= 2 and s4.startswith('0')) or int(s4) > 255: continue
                        ret.append('.'.join([s1, s2, s3, s4]))
        return ret


if __name__ == '__main__':
    s = Solution()
    ss = "010010"
    print(s.restoreIpAddresses(ss))
    print(s.restoreIpAddresses1(ss))
