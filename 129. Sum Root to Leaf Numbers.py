# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        stack = [(root, root.val)]
        total = 0
        
        while stack:
            current_node, current_val = stack.pop()
            if current_node:
                if not current_node.left and not current_node.right:
                    total += current_val
                if current_node.left:
                    stack.append((current_node.left, current_val*10+current_node.left.val))
                if current_node.right:
                    stack.append((current_node.right, current_val*10+current_node.right.val))
            
        return total
    
