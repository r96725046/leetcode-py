#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        res=(r-l)*min(height[l],height[r])
        while l<r:
            h=0
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
            res=max(res,(r-l)*min(height[l],height[r]))
        return res
# @lc code=end

