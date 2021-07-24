#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy=ListNode(0)
    
        while head is not None:
            tmp=dummy.next
            dummy.next=head
            head=head.next
            dummy.next.next=tmp
        
        return dummy.next
                
# @lc code=end

