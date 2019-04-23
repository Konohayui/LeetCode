# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def ListNodeToList(self, head):
        vals = []
        
        while head:
            vals.append(head.val)
            head = head.next
            
        return vals
    
    def ListToTree(self, left_idx, right_idx, values):
        if left_idx > right_idx:
            return None
        
        mid = (left_idx + right_idx)//2
        root = TreeNode(values[mid])
        
        if left_idx == right_idx:
            return root
        
        root.left = self.ListToTree(left_idx, mid - 1, values)
        root.right = self.ListToTree(mid+1, right_idx, values)
        
        return root
    
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        
        values = self.ListNodeToList(head)
        tree = self.ListToTree(0, len(values)-1, values)
        
        return tree
    
    
