#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
import functools
class Solution:
    # import functools
    # functools.cmp_to_key
    # return int(n2+n1)-int(n1+n2)
    def largestNumber(self, nums: List[int]) -> str:
        
        def compare(n1,n2):
            return int(n2+n1)-int(n1+n2)
        arr=[]
        for i in range(len(nums)):
            arr.append(str(nums[i]))

        arr.sort(key=functools.cmp_to_key(compare))
        res=""
        for i in range(len(arr)):
            if arr[i]=="0" and len(res)==0:
                continue
            res+=arr[i]

        return "0" if len(res) ==0 else res
# @lc code=end

