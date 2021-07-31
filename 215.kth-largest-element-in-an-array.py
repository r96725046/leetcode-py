#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums,k,0,len(nums)-1)

    def quickSelect(self,nums,k,l,r):
        start=l
        pivot=nums[r]
        for i in range(l,r):
            if nums[i]>pivot:
                nums[i],nums[start]=nums[start],nums[i]
                start+=1
        nums[start],nums[r]=nums[r],nums[start]

        if start==k-1:
            return nums[start]
        elif start<k-1:
            return self.quickSelect(nums,k,start+1,r)
        else:
            return self.quickSelect(nums,k,l,start-1)

# @lc code=end

