#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[]
        index=-1
        res=0
        for i in range(len(s)):

            if s[i]=='(':
                stack.append(i)
            else:
                if len(stack)==0:
                    index=i
                else:
                    stack.pop()
                    if len(stack)==0:
                        res=max(i-index,res)
                    else:
                        res=max(i-stack[-1],res)
        return res
# @lc code=end

