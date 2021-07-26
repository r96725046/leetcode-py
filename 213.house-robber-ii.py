#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.rob_house(nums,1,len(nums)),self.rob_house(nums,0,len(nums)-1))

    def rob_house(self, nums,l,r):
        pre1=0
        pre2=0
        cur=0
        for i in range(l,r):
            cur=max(nums[i]+pre1,pre2)
            pre1=pre2
            pre2=cur
        return cur

# @lc code=end

