#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    # 1.if index==len(word):
    #       return True
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited=[[0]*len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board,visited,word,0,i,j):
                    return True
        
        return False

    def dfs(self,board,visited,word,index,i,j):
        if index==len(word):
            return True

        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or visited[i][j]==1:
            return False
        if word[index]!=board[i][j]:
            return False
            
        visited[i][j]=1

        res=(self.dfs(board,visited,word,index+1,i-1,j) or
             self.dfs(board,visited,word,index+1,i,j-1) or
             self.dfs(board,visited,word,index+1,i+1,j) or
             self.dfs(board,visited,word,index+1,i,j+1))
        
        visited[i][j]=0
        return res
# @lc code=end

