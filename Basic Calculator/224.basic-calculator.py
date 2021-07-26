#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        sum=0
        sign=1
        i=0
        while i<len(s):
            c=s[i]
            if c=='+':
                sign=1
            elif c=='-':
                sign=-1
            elif c>='0' and c<='9':
                tmp=0
                while i<len(s):
                    c=s[i]
                    if c>='0' and c<='9':
                        tmp=tmp*10+(ord(c)-ord('0'))
                    else:
                        break
                    i+=1
                sum+=sign*tmp
                i-=1
            elif c=='(':
                stack.append(sum)
                stack.append(sign)
                sign=1
                sum=0
            elif c==')':
                sum=stack.pop()*sum+stack.pop()
            i+=1
        return sum

# @lc code=end

