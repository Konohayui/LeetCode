# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root_val = postorder.pop()
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        
        root.right = self.buildTree(inorder[inorder_idx+1:], postorder)
        root.left = self.buildTree(inorder[:inorder_idx], postorder)
        
        return root
    
    
