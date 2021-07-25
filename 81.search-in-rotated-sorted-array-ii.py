#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#

# @lc code=start
class Solution:
    # 1.if nums[mid]==target
    # 2.elif nums[mid]==nums[r]
    # 3.elif /nums[mid]<nums[r]
    # 4.else
    def search(self, nums: List[int], target: int) -> bool:
        l=0
        r=len(nums)-1

        while l<=r:

            mid=l+(r-l)//2
            if nums[mid]==target:
                return True
            elif nums[mid]==nums[r]:
                r-=1
            elif nums[mid]<nums[r]:
                if nums[mid]<target and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
            else:
                if nums[mid]>target and target>=nums[l]:
                    r=mid-1
                else:
                    l=mid+1
        return False    
# @lc code=end

