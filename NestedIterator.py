# @Time    : 2019/4/8 8:45
# @Author  : Xu Huipeng
# @Blog    : https://brycexxx.github.io/


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []
        self.idx = 0

        def flatten(nestedList):
            for elem in nestedList:
                if elem.isInteger():
                    self.queue.append(elem.getInteger())
                else:
                    sub_nest = elem.getList()
                    flatten(sub_nest)

        flatten(nestedList)

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            ret = self.queue[self.idx]
            self.idx += 1
            return ret
        return None

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx < len(self.queue):
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
