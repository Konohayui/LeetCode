# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        stack = [(root, total - root.val, [root.val])]
        
        while stack:
            curr, remainder, path = stack.pop()
            if not curr.left and not curr.right and remainder == 0:
                res.append(path)
            if curr.left:
                stack.append((curr.left, remainder - curr.left.val, path + [curr.left.val]))
            if curr.right:
                stack.append((curr.right, remainder - curr.right.val, path + [curr.right.val]))
                
        return res
    
    
