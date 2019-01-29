# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = str()
        num2 = str()
        
        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next
            
        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next
            
        total = str(int(num1[::-1]) + int(num2[::-1]))
        total = total[::-1]
        head = ListNode(total[0])
        result = head
        
        for i in range(1, len(total)):
            node = ListNode(total[i])
            head.next = node
            head = head.next
            
        return result
