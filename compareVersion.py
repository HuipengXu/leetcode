# @Time    : 2019/6/29 8:55
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_lst = version1.split('.')
        version2_lst = version2.split('.')
        v1_len, v2_len = len(version1_lst), len(version2_lst)
        if v1_len < v2_len:
            version1_lst.extend(['0'] * (v2_len - v1_len))
        elif v1_len > v2_len:
            version2_lst.extend(['0'] * (v1_len - v2_len))
        i = 0
        while i < len(version1_lst):
            if int(version1_lst[i]) < int(version2_lst[i]):
                return -1
            elif int(version1_lst[i]) > int(version2_lst[i]):
                return 1
            else:
                i += 1
        return 0
