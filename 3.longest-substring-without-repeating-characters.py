#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # max(index,dic[s[i]]+1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        res=index=0
        dic={}
        for i in range(len(s)):
            if s[i] in dic:
                index=max(index,dic[s[i]]+1)
            dic[s[i]]=i
            res=max(res,i-index+1)
        return res
# @lc code=end

