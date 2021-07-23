#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        fr=False
        fc=False

        for j in range(len(matrix[0])):
            if matrix[0][j]==0:
                fr=True
        for i in range(len(matrix)):
            if matrix[i][0]==0:
                fc=True
    
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    matrix[i][0]=0
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if fr:
            for j in range(0,len(matrix[0])):
                matrix[0][j]=0
        if fc:
            for i in range(0,len(matrix)):
                matrix[i][0]=0
# @lc code=end

