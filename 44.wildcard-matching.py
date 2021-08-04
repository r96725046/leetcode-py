#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[0]*(len(p)+1) for _ in range(len(s)+1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if (dp[i-1][j-1] and s[i-1]==p[j-1]) or p[j-1]=="?":
                    dp[i][j]=1
                elif p[j-1]=="*":
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=0
        if dp[len(s)][len(p)]==0:
            return False
        else:
            return True
# @lc code=end

