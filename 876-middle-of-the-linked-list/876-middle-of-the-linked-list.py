# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ''' 
        this is a pointers based question: slow pointer and fast pointer 
        slow: move 1 step in each eteration
        fast: move 2 steps 
        when fast is at the end, then slow is at the middle 
        '''
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow 
            
                
            
            
        