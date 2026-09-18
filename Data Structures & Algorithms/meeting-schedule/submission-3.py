"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if len(intervals) < 2:
            return True

        # lst = [[intv.start, intv.end]for intv in intervals]

        lst = intervals

        lst.sort(key=lambda x: x.start)

        for i in range(1, len(lst)):
            if lst[i - 1].end > lst[i].start:
                return False

        return True
