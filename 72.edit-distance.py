#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        arr=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
       
        for i in range(len(arr)):
            arr[i][0]=i     
        for j in range(len(arr[0])):
            arr[0][j]=j
      
        for i in range(1,len(arr)):
            for j in range(1,len(arr[0])):
                if word1[i-1]==word2[j-1]:
                    arr[i][j]=arr[i-1][j-1]
                else:
                    arr[i][j]=min(arr[i-1][j-1],arr[i-1][j],arr[i][j-1])+1
        return arr[-1][-1]
# @lc code=end

