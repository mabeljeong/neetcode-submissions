"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool: 
        #sort by start val 
        intervals.sort(key=lambda x:x.start)

        for i in range(len(intervals)-1): #() 
            if intervals[i].end - intervals[i+1].start > 0: 
                return False 
        return True


