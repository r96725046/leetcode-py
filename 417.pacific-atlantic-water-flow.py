#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
class Solution:
    # 2 visited array
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        h=heights
        row=len(h)
        col=len(h[0])
        p=[[0]*col for _ in range(row)]
        a=[[0]*col for _ in range(row)]
        for i in range(row):
            self.dfs(h,i,0,h[i][0],p)
            self.dfs(h,i,col-1,h[i][col-1],a)

        for j in range(col):
            self.dfs(h,0,j,h[0][j],p)
            self.dfs(h,row-1,j,h[row-1][j],a)
        
        for i in range(row):
            for j in range(col):
                if p[i][j] and a[i][j]:
                    res.append([i,j])
        return res

    def dfs(self,heights,i,j,pre,visited):
        if i<0 or j<0 or i>=len(heights) or j>=len(heights[0]):
            return 
        if visited[i][j] or pre>heights[i][j]:
            return 
        cur=heights[i][j]
        visited[i][j]=True
        self.dfs(heights,i+1,j,cur,visited)
        self.dfs(heights,i,j+1,cur,visited)
        self.dfs(heights,i-1,j,cur,visited)
        self.dfs(heights,i,j-1,cur,visited)
    
# @lc code=end

