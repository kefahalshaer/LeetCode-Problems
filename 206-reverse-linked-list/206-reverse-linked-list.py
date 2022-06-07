# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head and head.next != None:
            curr, prev = head, None  # 2 pointers
            while curr:
                nxt  = curr.next # to store the value of curr.next 
                curr.next = prev 
                prev = curr
                curr = nxt
            return prev  
        return head