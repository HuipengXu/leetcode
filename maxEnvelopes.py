# @Time    : 2019/5/16 12:41
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

from typing import List
from functools import cmp_to_key


class Solution:
    # 超时
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes or not envelopes[0]: return 0
        envelopes.sort()
        dp = [1] * len(envelopes)
        ret = 1
        for i in range(1, len(envelopes)):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] \
                        and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ret = max(ret, dp[i])
        return ret

    # 二分法牛逼啊
    def maxEnvelopes1(self, envelopes: List[List[int]]) -> int:
        nums = sorted(envelopes, key=cmp_to_key(lambda x, y: x[0] - y[0] if x[0] != y[0] else y[1] - x[1]))
        size = len(nums)
        dp = []
        for x in range(size):
            low, high = 0, len(dp) - 1
            while low <= high:
                mid = low + ((high - low) >> 1)
                if dp[mid][1] < nums[x][1]:
                    low = mid + 1
                else:
                    high = mid - 1
            if low < len(dp):
                dp[low] = nums[x]
            else:
                dp.append(nums[x])
        return len(dp)


if __name__ == '__main__':
    envelopes = [[5, 4], [6, 4], [5, 5], [6, 7], [2, 18], [10, 9]]
    s = Solution()
    print(s.maxEnvelopes(envelopes))
    print(s.maxEnvelopes1(envelopes))
