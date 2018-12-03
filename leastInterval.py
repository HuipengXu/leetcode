"""
利用插空法，首先找到频率最高的任务，然后按照要求的冷却时间隔开，中间插入其他任务；
如果冷却时间过短，由最频繁任务构建的空间不足以放入其他任务时，实际上在尾部完全可以
分别间隔实行完成不需要多余的冷却时间，此时所需最短时间就是任务的长度
"""

class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        length = len(tasks)
        if length == 1:
            return 1
        if n == 0:
            return length
        task_freq = Counter(tasks).most_common()
        most_freq = task_freq[0]
        time = (n + 1) * (most_freq[1] - 1)
        for _, f in task_freq:
            if f == most_freq[1]:
                time += 1
        return max(length, time)