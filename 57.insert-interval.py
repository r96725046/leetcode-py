#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda a:a[0])

        for cur in intervals:
            if cur[0]>newInterval[1]:
                res.append(newInterval)
                newInterval=cur
            elif cur[1]<newInterval[0]:
                res.append(cur)
            else:
                newInterval[0]=min(cur[0],newInterval[0])
                newInterval[1]=max(cur[1],newInterval[1])

        res.append(newInterval)
        return res
# @lc code=end

