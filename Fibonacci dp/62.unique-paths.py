#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        arr=[[0]*(n+1) for _ in range(m+1)]

        for i in range(1,len(arr)):
            for j in range(1,len(arr[0])):
                if i==1 and j==1:
                    arr[i][j]=1
                else:
                    arr[i][j]=arr[i-1][j]+arr[i][j-1]
        
        return arr[-1][-1]
# @lc code=end

