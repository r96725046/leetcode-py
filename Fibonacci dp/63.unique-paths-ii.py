#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid
        arr=[[0]*(len(grid[0])+1) for _ in range(len(grid)+1)]
        if grid[0][0]==1:
            return 0
        for i in range(1,len(arr)):
            for j in range(1,len(arr[0])):
                if i==1 and j==1:
                    arr[i][j]=1
                elif grid[i-1][j-1]==1:
                    arr[i][j]=0
                else:
                    arr[i][j]=arr[i-1][j]+arr[i][j-1]
        return arr[len(grid)][len(grid[0])]
# @lc code=end

