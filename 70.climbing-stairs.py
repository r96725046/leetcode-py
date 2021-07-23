#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return 1
        arr=[0]*(n+1)
        arr[0]=1
        arr[1]=1
        for i in range(2,len(arr)):
            arr[i]=arr[i-1]+arr[i-2]

        return arr[n]

# @lc code=end

