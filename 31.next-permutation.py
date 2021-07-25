#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#

# @lc code=start
class Solution:
    # Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
    # Find the largest index l > k such that nums[k] < nums[l].
    # Swap nums[k] and nums[l].
    # Reverse the sub-array nums[k + 1:].
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                index=i-1
                break
        if index<0:
            nums.reverse()
            return

        for i in range(len(nums)-1,index,-1):
            if nums[i]>nums[index]:
                self.swap(nums,index,i)
                break

        l=index+1
        r=len(nums)-1
        while l<r:
            self.swap(nums,l,r)
            l+=1
            r-=1

    def swap(self,nums,l,r):
        tmp=nums[l]
        nums[l]=nums[r]
        nums[r]=tmp
# @lc code=end

