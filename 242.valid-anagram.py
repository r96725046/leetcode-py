#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}

        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        for c in t:
            if c not in dic:
                return False
            else:
                dic[c]-=1
        for k in dic.keys():
            if dic[k]!=0:
                return False
        return True
# @lc code=end

