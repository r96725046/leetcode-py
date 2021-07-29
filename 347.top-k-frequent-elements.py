#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    # k-=len(arr[i])
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr=[[] for _ in range(len(nums)+1)]

        dic={}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]]+=1
            else:
                dic[nums[i]]=1
        for key in dic.keys():
            arr[dic[key]].append(key)
        
        res=[]
        for i in range(len(arr)-1,-1,-1):
            if k==0: break
            if len(arr[i])>0:
                res+=arr[i]
                k-=len(arr[i])
           
        return res
# @lc code=end

