class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        # scores = [0, 0]
        scores= []
        for record in ops:
            if record == '+':
                score = scores[-1] + scores[-2]
                scores.append(score)
            elif record == 'D':
                score = 2 * scores[-1]
                scores.append(score)
            elif record == 'C':
                scores.pop()
            else:
                score = int(record)
                scores.append(score)
        return sum(scores)
                