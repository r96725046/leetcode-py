#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda a:a[0])

        interval=intervals[0]

        for i in range(1,len(intervals)):
            cur=intervals[i]
            if cur[0]>interval[1]:
                res.append(interval)
                interval=cur
            else:
                interval[0]=min(cur[0],interval[0])
                interval[1]=max(cur[1],interval[1])
        
        res.append(interval)
        return res
# @lc code=end

