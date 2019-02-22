# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        full_list = []
        dummy = ListNode(0)
        res = dummy
        
        for l in lists:
            while l is not None:
                full_list.append(l.val)
                l = l.next
        
        for val in sorted(full_list):
            dummy.next = ListNode(val)
            dummy = dummy.next
            
        return res.next
        
        
