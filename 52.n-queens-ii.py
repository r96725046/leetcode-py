#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(row):
            if row==n:
                self.ount+=1
                return
            for j in range(n):
                if j in col or row+j in d1 or row-j in d2:
                    continue
                col.add(j)
                d1.add(row+j)
                d2.add(row-j)
                dfs(row+1)
                col.remove(j)
                d1.remove(row+j)
                d2.remove(row-j)
        self.count=0
        col=set()
        d1=set()
        d2=set()
        dfs(0)
        return self.count

# @lc code=end

