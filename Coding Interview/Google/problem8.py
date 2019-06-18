"""
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
#     def isUnivalhelper(self, root):
#         if root == None:
#             return True
        
#         if root.left != None and root.val != root.left.val:
#             return False
#         elif root.right != None and root.val != root.right.val:
#             return False
#         elif self.isUnivalhelper(root.left) and self.isUnivalhelper(root.right):
#             return True
            
#         return False
    
#     def isUnivalTree(self, root: TreeNode) -> bool:
#         return self.isUnivalhelper(root)
    
    def CountHelper(self, root):
        if not root:
            return 0, True
        left_count, subLeft = self.CountHelper(root.left)
        right_count, subRight = self.CountHelper(root.right)
        total = left_count + right_count
        if subLeft and subRight:
            if root.left != None and root.val != root.left.val:
                return total, False
            elif root.right != None and root.val != root.right.val:
                return total, False
            return total + 1, True
        return total, False
    
    def subUnivalTreeCount(self, root):
        total, _ =  self.CountHelper(root)
        return total
        
    
