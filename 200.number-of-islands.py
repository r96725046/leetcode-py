#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    # No visited arr
    # set cell to "0"
    def numIslands(self, grid: List[List[str]]) -> int:
        
        visited=[[0] * len(grid[0]) for _ in range(len(grid))]
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1":
                    self.dfs(grid,i,j)
                    res+=1
        return res

    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]=="0":
            return 
        grid[i][j]="0"

        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)

# @lc code=end

