#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    #  **
    #  left && right arr =>find the heights[j] smaller than heights[i]
    #  1.left[0]=-1 and right[right.length-1]=right.length;
    #  2.for i++; j=i-1 while j--, for i--; j=i+1 while j++
    def largestRectangleArea(self, heights: List[int]) -> int:
        left=[0]*len(heights)
        right=[0]*len(heights)

        left[0]=-1

        for i in range(1,len(heights)):
            j=i-1
            while j>=0:
                if(heights[j]>=heights[i]):
                    j=left[j]
                else:
                    break
            left[i]=j
        right[len(heights)-1]=len(heights)
        for i in range(len(heights)-1,-1,-1):
            j=i+1
            while j<len(heights):
                if(heights[j]>=heights[i]):
                    j=right[j]
                else:
                    break
            right[i]=j
        
        res=0

        for i in range(len(left)):
            res=max(res,(right[i]-left[i]-1)*heights[i])
        return res
# @lc code=end

