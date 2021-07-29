#
# @lc app=leetcode id=85 lang=python3
#
# [85] Maximal Rectangle
#

# @lc code=start
class Solution:
    # 1D array
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix)==0: return 0
        arr=[0]*len(matrix[0])
        res=0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]=='1':
                    arr[j]+=1
                else:
                    arr[j]=0
            res=max(res,self.maxHistgram(arr))
        return res

    def maxHistgram(self, arr):

        left=[0]*len(arr)
        right=[0]*len(arr)

        left[0]=-1

        for i in range(1,len(left)):
            j=i-1
            while j>=0:
                if arr[j]>=arr[i]:
                    j=left[j]
                else:
                    break
            left[i]=j

        right[-1]=len(right)

        for i in range(len(right)-1,-1,-1):
            j=i+1
            while j<len(right):
                if arr[j]>=arr[i]:
                    j=right[j]
                else:
                    break
            right[i]=j

        res=0
        for i in range(len(left)):
            res=max(res,(right[i]-left[i]-1)*arr[i])
        return res
# @lc code=end

