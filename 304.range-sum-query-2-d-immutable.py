#
# @lc app=leetcode id=304 lang=python3
#
# [304] Range Sum Query 2D - Immutable
#

# @lc code=start
class NumMatrix:
    # matrix[i-1][j-1]
    def __init__(self, matrix: List[List[int]]):
        self.res=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for i in range(1,len(self.res)):
            for j in range(1,len(self.res[0])):
                    self.res[i][j]=self.res[i-1][j]+matrix[i-1][j-1]

        for j in range(1,len(self.res[0])):
            for i in range(len(self.res)):
                self.res[i][j]+=self.res[i][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.res[row2+1][col2+1]-self.res[row1][col2+1]-self.res[row2+1][col1]+self.res[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

