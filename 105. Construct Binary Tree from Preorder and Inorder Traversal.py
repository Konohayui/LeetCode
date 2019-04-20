# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        inorder_idx = inorder.index(root_val)
        
        root.left = self.buildTree(preorder, inorder[:inorder_idx])
        root.right = self.buildTree(preorder, inorder[inorder_idx+1:])
        
        return root
    
    
