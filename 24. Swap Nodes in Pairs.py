# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        position = 0
        previous = head
        track = head
        
        while track:
            position += 1
            
            if position % 2 == 0:
                previous_val = previous.val
                previous.val = track.val
                track.val = previous_val
                previous = track.next
                
            track = track.next
        return head
        
        
