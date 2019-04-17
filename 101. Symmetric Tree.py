# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, node1, node2):
        if not node1 and not node2:
            return True
        
        if node1 and node2 and node1.val == node2.val:
            return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
        return False
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or self.helper(root.left, root.right)
    
