#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if mid>0 and nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]<nums[r]:
                r=mid-1
            else:
                l=mid+1

        return nums[mid]
# @lc code=end

