#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    # ***
    # https://www.cnblogs.com/grandyang/p/4373533.html
    # when i reach over last, update last to cur
    # and res++
    # cur=max(cur,i+nums[i])
    def jump(self, nums: List[int]) -> int:
        last,cur,res=0,0,0
        for i in range(len(nums)):
            if i>last:
                res+=1
                last=cur
            cur=max(cur,i+nums[i])
        
        return res
# @lc code=end

