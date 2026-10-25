class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        Input: intervals = [[1,3],[4,6]], newInterval = [2,5]
                                    i

        intv = [4,6]

        stack = [[1, 6]]

        last_intv = [1, 3]

        newInterval = [min(1, 4, 2),max(6, 3, 5)] = [1, 6]


        """
        
        stack = []

        for i, intv in enumerate(intervals):
            if intv[1] < newInterval[0]:
                stack.append(intv)

            elif intv[0] > newInterval[1]:
                stack.append(newInterval)
                return stack + intervals[i:]

            else:

                newInterval = [min(intv[0], newInterval[0]), max(intv[1], newInterval[1])]

        stack.append(newInterval)

        return stack