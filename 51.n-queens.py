#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
class Solution:
    # *** 
    # check    
    #          \  |  / 
    #          .  Q  .
    #          .  .  .
    # inner function
    # check column in each row
    # if valid then traverse next row
    # res.append([''.join(row) for row in m])
    def solveNQueens(self, n: int) -> List[List[str]]:

        def dfs(row):
            if row==n:
                res.append([''.join(row) for row in m])
                return 
            for j in range(n):
                if valid(row,j):
                    m[row][j]='Q'
                    dfs(row+1)
                    m[row][j]='.'
        
        def valid(row,col):
            for i in range(row):
                if m[i][col]=='Q':return False
            i=row-1
            j=col-1
            while i>=0 and j>=0:
                if m[i][j]=='Q': return False
                i-=1
                j-=1
            i=row+1
            j=col+1
            while i<n and j<n:
                if m[i][j]=='Q': return False
                i+=1
                j+=1 
            return True

        res=[]
        m=[['.']*n for _ in range(n)]
        dfs(0)
        return res
        
# @lc code=end

