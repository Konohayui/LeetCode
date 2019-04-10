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
        pre = dummy
        dummy.next = head
        
        while head and head.next:
            while head and head.next and head.val == head.next.val:
                head = head.next
            
            if pre.next == head:
                pre = head
                
            else:
                pre.next = head.next
            head = head.next
            
        return dummy.next
                
