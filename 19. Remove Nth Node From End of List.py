# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        _head = ListNode(0)
        _head.next = head
        length = 1

        while head.next != None:
            length += 1
            head = head.next
        
        remove_idx = length - n
        head = _head
        idx = 0
        
        while head.next != None:
            if idx == remove_idx:
                head.next = head.next.next
                break
            head = head.next
            idx += 1
            
        return _head.next
