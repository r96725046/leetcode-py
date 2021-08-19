#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def solve(board,row,col,s):
            if row==9:return True
            if col==9:return solve(board,row+1,0,s)
            if board[row][col]!='.':return solve(board,row,col+1,s)
            for k in range(1,10):
                v="#"+str(k)+"#"
                r=str(row)+v
                c=v+str(col)
                cl=str(row//3)+v+str(col//3)
                if r in s or c in s or cl in s:continue
                s.add(r)
                s.add(c)
                s.add(cl)
                board[row][col]=str(k)
                if(solve(board,row,col+1,s)):return True
                board[row][col]='.'
                s.remove(r)
                s.remove(c)
                s.remove(cl)
            return False    
        s=set()
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.':
                    v="#"+board[i][j]+"#"
                    s.add(str(i)+v)
                    s.add(v+str(j))
                    s.add(str(i//3)+v+str(j//3))

        solve(board,0,0,s)       
# @lc code=end

