#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        res=[0]*(n+1)
        res[1]=1
        
        for i in range(2,n+1):
            res[i]=res[i-1]+res[i-2]

        return res[n]
# @lc code=end

