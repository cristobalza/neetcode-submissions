class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        stack = []

        for i, curr in enumerate(intervals):
            if curr[1] < newInterval[0]:
                stack.append(curr)

            elif curr[0] > newInterval[1]:
                stack.append(newInterval)
                return stack + intervals[i:]

            else:

                newInterval = [min(curr[0], newInterval[0]), max(curr[1], newInterval[1])]

        stack.append(newInterval)

        return stack
        