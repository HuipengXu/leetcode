# @Time    : 2019/5/10 18:19
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/

class Solution:
    def simplifyPath(self, path: str) -> str:
        ret = []
        dirs = [d for d in path.split('/') if d != '']
        for d in dirs:
            if d == '..' and len(ret) > 0:
                ret.pop()
            elif d != '..' and d != '.':
                ret.append(d)
        return '/' + '/'.join(ret)


if __name__ == '__main__':
    s = Solution()
    ss = "/a/./b/../../c/"
    print(s.simplifyPath(ss))
