#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    # arr[0]=0
    # i-coin>=0
    # arr[i-coin]+1
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr=[amount+1]*(amount+1)
        arr[0]=0

        for i in range(amount+1):
            for coin in coins:
                if i-coin>=0:
                    arr[i]=min(arr[i],arr[i-coin]+1)

        if arr[amount]==amount+1:
            return -1
        else:
            return arr[amount]
# @lc code=end

