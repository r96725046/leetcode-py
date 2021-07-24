#
# @lc app=leetcode id=295 lang=python3
#
# [295] Find Median from Data Stream
#

# @lc code=start

class MedianFinder:
    # heappush heappop
    # max => -num
    # min => num
    # self
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxHeap=[]
        self.minHeap=[]

    def addNum(self, num: int) -> None:
        heappush(self.maxHeap,-num)
        heappush(self.minHeap,-heappop(self.maxHeap))
        if len(self.minHeap)>len(self.maxHeap):
            heappush(self.maxHeap,-heappop(self.minHeap))

    def findMedian(self) -> float:
        if len(self.maxHeap)>len(self.minHeap):
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0]+self.minHeap[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# @lc code=end

