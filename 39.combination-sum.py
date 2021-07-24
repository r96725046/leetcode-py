#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        if candidates is None or len(candidates)==0:
            return []
            
        self.backtrack(candidates,[],0,target,res)
        return res

    def backtrack(self,arr,cur,start,target,res):
        if target<0:
            return
        if target == 0:
            res.append(list(cur))

        for i in range(start,len(arr)):
            cur.append(arr[i])
            self.backtrack(arr,cur,i,target-arr[i],res)
            cur.pop()
# @lc code=end

