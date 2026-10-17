class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """

        intervals = [[1,2],[2,4],[1,4]]

        Assumptions:
            That if the end of the interval and the start of the interval are the same, then they are NOT overlapping

            They are not sorted O(nlogn)






        1. 2  

        1.     4

           2.  4


        stack = []

        interval = [1, 4]

        last_interval = [1, 2]

        res ++





        """

        res = 0

        stack = []

        intervals.sort(key=lambda x: x[0])

        for i, intv in enumerate(intervals):
            if stack and stack[-1][1] > intv[0]:

                last_interval = stack.pop()

                new_interval = [min(last_interval[0], intv[0]), min(last_interval[1], intv[1])]

                res += 1

                stack.append(new_interval)

            else:
                stack.append(intv)

        return res





        