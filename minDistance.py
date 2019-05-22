# @Time    : 2019/5/22 9:03
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        for i in range(len(word1) + 1):
            dp[i][0] = i
        for i in range(len(word2) + 1):
            dp[0][i] = i
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    s1 = dp[i - 1][j - 1]
                    # 删除
                    s2 = dp[i - 1][j]
                    # 插入
                    s3 = dp[i][j - 1]
                    dp[i][j] = min(s1, s2, s3) + 1
        return dp[-1][-1]

    # 空间优化
    def minDistance1(self, word1: str, word2: str) -> int:
        dp = [i for i in range(len(word2) + 1)]
        for i in range(1, len(word1) + 1):
            left_upper = dp[0]
            dp[0] = i
            for j in range(1, len(word2) + 1):
                if word2[j - 1] == word1[i - 1]:
                    tmp = dp[j]
                    dp[j] = left_upper
                    left_upper = tmp
                else:
                    replace = left_upper
                    delete = dp[j]
                    insert = dp[j - 1]
                    left_upper = dp[j]
                    dp[j] = min(replace, delete, insert) + 1
        return dp[-1]

    # 超时
    def minDistance2(self, word1: str, word2: str) -> int:
        def recur(word1: str, word2: str) -> int:
            if not word1: return len(word2)
            if not word2: return len(word1)
            if word1[-1] == word2[-1]:
                return recur(word1[:-1], word2[:-1])
            else:
                replace = recur(word1[:-1], word2[:-1])
                delete = recur(word1[:-1], word2)
                insert = recur(word1, word2[:-1])
                return min(replace, delete, insert) + 1

        return recur(word1, word2)

    # 记忆优化
    def minDistance3(self, word1: str, word2: str) -> int:
        memo = [[0] * len(word2) for _ in range(len(word1))]

        def recur(i: int, j: int) -> int:
            if i < 0: return j + 1
            if j < 0: return i + 1
            if memo[i][j] > 0: return memo[i][j]
            if word1[i] == word2[j]:
                memo[i][j] = recur(i - 1, j - 1)
            else:
                replace = recur(i - 1, j - 1)
                delete = recur(i - 1, j)
                insert = recur(i, j - 1)
                memo[i][j] = min(replace, delete, insert) + 1
            return memo[i][j]

        return recur(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    word1 = "intention"
    word2 = "execution"
    s = Solution()
    print(s.minDistance(word1, word2))
