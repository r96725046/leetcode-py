#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)*len(matrix[0])-1

        while l<=r:
            mid=int((l+r)//2)
            value=matrix[mid//len(matrix[0])][mid%len(matrix[0])]
            if value==target:
                return True
            elif value>target:
                r=mid-1
            else:
                l=mid+1

        return False
# @lc code=end

