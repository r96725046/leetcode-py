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
                self.swap(nums,i,start)
                start+=1
        self.swap(nums,start,r)

        if start==k-1:
            return nums[start]
        elif start<k-1:
            return self.quickSelect(nums,k,start+1,r)
        else:
            return self.quickSelect(nums,k,l,start-1)

    def swap(self,nums,l,r):
        tmp=nums[l]
        nums[l]=nums[r]
        nums[r]=tmp

# @lc code=end

