class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals.sort(key=lambda x: x[0])

        res = 0

        stack = []
        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            if stack[-1][1] > intervals[i][0]:
                res += 1

                last_intv = stack.pop()

                new_intv = [intervals[i][0], min(intervals[i][1], last_intv[1])]

                stack.append(new_intv)

            else:
                stack.append(intervals[i])

        return res