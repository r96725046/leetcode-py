#
# @lc app=leetcode id=384 lang=python3
#
# [384] Shuffle an Array
#

# @lc code=start
import random
class Solution:
    # https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
    arr=None
    def __init__(self, nums: List[int]):
        self.arr=nums
       
    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return list(self.arr)

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res=list(self.arr)
        for i in range(len(res)-1,0,-1):
            j=random.randrange(0,i+1)
            res[i],res[j]=res[j],res[i]
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
# @lc code=end

