#
# @lc app=leetcode id=124 lang=python3
#
# [124] Binary Tree Maximum Path Sum
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
       self.res=float("-inf")
       self.dfs(root)
       return self.res

    def dfs(self,node):
        if node is None:
            return 0

        l=self.dfs(node.left)
        r=self.dfs(node.right)

        cur=max(node.val,node.val+l,node.val+r)
        self.res=max(self.res,cur,node.val+l+r)
        return cur

# @lc code=end

