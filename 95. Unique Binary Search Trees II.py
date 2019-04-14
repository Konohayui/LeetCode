# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generator(self, elements):
        if not elements:
            return [None]
            
        res = []
        for i in range(len(elements)):
            lefts, rights = self.generator(elements[:i]), self.generator(elements[i+1:])
            for l in lefts:
                for r in rights:
                    root, root.left, root.right = TreeNode(elements[i]), l, r
                    res += root,
                        
        return res
    
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []
        
        elements = list(range(1, n+1))
        res = self.generator(elements)
        
        return res
        
