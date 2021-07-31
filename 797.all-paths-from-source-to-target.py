#
# @lc app=leetcode id=797 lang=python3
#
# [797] All Paths From Source to Target
#

# @lc code=start
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res=[]
        self.dfs(graph,0,[0],res)
        return res

    def dfs(self,graph,index,cur,res):

        if index==len(graph)-1:
            res.append(list(cur))
            return

        nodes=graph[index]
        for i in range(len(nodes)):
            cur.append(nodes[i])
            self.dfs(graph,nodes[i],cur,res)
            cur.pop()


# @lc code=end

