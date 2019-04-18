# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res, level = [], [root]
        while root and level:
            res += [node.val for node in level],
            node_pairs = [(node.left, node.right) for node in level]
            level = [child for pair in node_pairs for child in pair if child]
            
        return res
    
