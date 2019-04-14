# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res += root.val,
            self.helper(root.right, res)
            
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        
        return res
    
