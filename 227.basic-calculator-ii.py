#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    # stack.append(int(stack.pop()/tmp))
    def calculate(self, s: str) -> int:
        stack=[]
        sum=0
        sign='+'
        i=0
        while i<len(s):
            c=s[i]
            if c>='0' and c<='9':
                tmp=0
                while i<len(s):
                    c=s[i]
                    if c>='0' and c<='9':
                        tmp=tmp*10+(ord(c)-ord('0'))
                    else:
                        break
                    i+=1
                i-=1
                if sign=='+':
                    stack.append(tmp)
                elif sign=='-':
                    stack.append(-tmp)
                elif sign=='*':
                    stack.append(stack.pop()*tmp)
                elif sign=='/':
                    stack.append(int(stack.pop()/tmp))
            elif c==' ':
                i+=1
                continue
            else:
                sign=c
            i+=1
        while len(stack)>0:
            sum+=stack.pop()
        return sum
# @lc code=end

