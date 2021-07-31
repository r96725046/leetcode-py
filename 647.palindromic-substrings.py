#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res=0
        for i in range(len(s)):
            res+=self.check(s,i,i)
            res+=self.check(s,i,i+1)
        
        return res

    def check(self,s,i,j): 
        count=0
        while i>=0 and j<len(s):
            if s[i]!=s[j]:
                break
            i-=1
            j+=1
            count+=1

        return count
# @lc code=end

