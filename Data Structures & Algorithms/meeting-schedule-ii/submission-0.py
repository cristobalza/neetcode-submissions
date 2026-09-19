"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """

        intervals = [(0,40),(5,10),(15,20)]
                               i

        stack = [(0,40)]



        """

        i, j = 0, 0

        res, count = 0, 0

        start_sorted_intervals = sorted(intervals, key=lambda x: x.start)
        end_sorted_intervals = sorted(intervals, key=lambda x: x.end)

        while i < len(intervals):
            if start_sorted_intervals[i].start < end_sorted_intervals[j].end:
                count += 1
                i += 1

            else:
                count -= 1
                j += 1

            res = max(res, count)

        return res