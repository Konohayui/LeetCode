# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        depth = 0
        level = [root]
        
        while level:
            depth += 1
            node_pairs = [(leaf.left, leaf.right) for leaf in level]
            level = [child for pair in node_pairs for child in pair if child]
            
        return depth
        
