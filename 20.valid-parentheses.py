#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for i in range(len(s)):
            char=s[i]
            if char=="{" or char=="(" or char=="[":
                stack.append(char)
            else:
                if(len(stack)==0):
                    return False
                elif stack[-1]=="{" and char!="}":
                    return False
                elif stack[-1]=="(" and char!=")":
                    return False
                elif stack[-1]=="[" and char!="]":
                    return False
                else:
                    stack.pop()
        return len(stack)==0
# @lc code=end

