#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0]=True
        for j in range(1,len(dp[0])):
            if dp[0][j-1] and p[j-1]=="*":
                dp[0][j]=True

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
                    
        return dp[-1][-1]

# @lc code=end

