#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        nums.reverse()
        def reversePos(nums, i, j):
            while i<j:
                tmp=nums[i]
                nums[i]=nums[j]
                nums[j]=tmp
                i+=1
                j-=1
        reversePos(nums,0,k-1)
        reversePos(nums,k,len(nums)-1)        
# @lc code=end

