# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        res, level = [], [root]
        depth = 0
        
        while level:
            depth += 1
            current_val = []
            next_level = []
            
            for node in level:
                current_val += node.val,
                if node.left:
                    next_level += node.left,
                if node.right:
                    next_level += node.right,
            level = next_level
            
            if depth % 2 == 0:
                current_val = current_val[::-1]
            res += current_val,
                
        return res
    
