# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_paths(self, root: TreeNode, remainder: int, res: List[bool]) -> bool:
        if root:
            if not root.left and not root.right:
                if root.val == remainder:
                    res.append(True)
                
            if root.left:
                self.find_paths(root.left, remainder-root.val, res)
            if root.right:
                self.find_paths(root.right, remainder-root.val, res)
                
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            return False
        
        res = []
        self.find_paths(root, total, res)
        
        return any(res)
    
    
