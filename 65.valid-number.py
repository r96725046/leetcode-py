#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid numsber
#

# @lc code=start
class Solution:
    # ***
    # 1
    # Skip spaces
    # Check '+'/'-'
    # Check digital(can contain ".")
    # Check exponent
    #  a. Check '+'/'-'
    #  b. Check digital(cannot contain ".")
    # Check space
    def isnumsber(self, s: str) -> bool:
        
        i=0
        
        if s[i]=='+' or s[i]=='-':
            i+=1

        dot=0
        nums=0
        while i<len(s):    
            if s[i]>='0' and s[i]<='9':
                nums+=1
            elif s[i]=='.':
                dot+=1
            else:
                break
            i+=1
        if nums==0 or dot>1:
            return False

        if i<len(s):
            if s[i]=='e' or s[i]=='E':
                i+=1
                sign=0
                nums=0
                while i<len(s):
                    if s[i]>='0' and s[i]<='9':
                        nums+=1
                    elif s[i]=='+' or s[i]=='-':
                        if nums>0: return False
                        sign+=1
                    else:
                        return False
                    i+=1
                if sign>1 or nums==0:
                    return False
            else:
                return False
        return True
# @lc code=end

