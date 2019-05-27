# @Time    : 2019/5/27 8:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def countAndSay(self, n: int) -> str:
        cur = '1'
        for _ in range(n - 1):
            res = []
            cnt = m = j = 0
            while j < len(cur):
                if cur[j] == cur[m]:
                    cnt += 1
                    j += 1
                    if j == len(cur):
                        res.append(str(cnt) + cur[m])
                    continue
                res.append(str(cnt) + cur[m])
                cnt = 0
                m = j
            cur = ''.join(res)
        return cur


if __name__ == '__main__':
    s = Solution()
    print(s.countAndSay(5))
