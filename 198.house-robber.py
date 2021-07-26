#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    # ***
    # pre1=i-2
    # pre2=i-1
    # cur will rob or not rob
    def rob(self, nums: List[int]) -> int:
        pre1=0
        pre2=0
        cur=0
        for i in range(0,len(nums)):
            cur=max(nums[i]+pre1,pre2)
            pre1=pre2
            pre2=cur
        return cur

# @lc code=end

