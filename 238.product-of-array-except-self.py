#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    # nums  1  2  3  4
    # res   1  1  2  6   

    # pre 1 1  2  6  - 
    
    # res  1*24 1*12 2*4 6*1
    # pre    -   24   12  4  1  

    # 1.pre =1 ,res[i]=pre
    # 2.pre =1 ,res*=pre and pre*=nums[i] for next i
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]

        pre=1
        for i in range(len(nums)):
            res.append(pre)
            pre=nums[i]*pre

        pre=1
        for i in range(len(nums)-1,-1,-1):
            res[i]*=pre
            pre*=nums[i]
        return res

# @lc code=end

