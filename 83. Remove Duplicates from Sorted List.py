# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        dummy = ListNode(None)
        dummy.next = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
                
            else:
                head = head.next
                
        return dummy.next
    
