#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # run 0~n
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        fast=dummy
        slow=dummy

        while n>=0:
            fast=fast.next
            n-=1

        while fast!=None:
            fast=fast.next
            slow=slow.next

        slow.next=slow.next.next
        return dummy.next
# @lc code=end

