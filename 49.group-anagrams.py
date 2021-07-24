#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}

        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            key=""
            for i in count:
                key+=str(i)+"#"
            
            if key not in res:
                res[key]=[s]
            else:
                res[key].append(s)
      
        return res.values()
# @lc code=end

