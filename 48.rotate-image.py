#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
class Solution:
    # i 0~n
    # j i~n
    # swap(matrix[i][j],matrix[j][i])
    # swap(l,r)
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                tmp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=tmp
        
        for i in range(n):
            l=0
            r=n-1
            while l<r:
                tmp=matrix[i][l]
                matrix[i][l]=matrix[i][r]
                matrix[i][r]=tmp
                l+=1
                r-=1
# @lc code=end

