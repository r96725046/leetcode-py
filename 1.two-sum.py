#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            if d.get(target-nums[i]) is None:
                d[nums[i]]=i
            else:
                res.append(i)
                res.append(d.get(target-nums[i]))
                return res
        return res
# @lc code=end

