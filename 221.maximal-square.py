#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    # min min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp=[[0]*(len(matrix[0])+1) for _ in range(len(matrix)+1)]
        res=0
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if matrix[i-1][j-1]=='0':
                    dp[i][j]=0
                else:
                    dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                res=max(res,dp[i][j])   
                
        return res*res
# @lc code=end

