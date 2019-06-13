# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        values = []
        def serializer(node):
            if node:
                values.append(str(node.val))
                serializer(node.left)
                serializer(node.right)
            else:
                values.append("#")
                
        serializer(root)
        return " ".join(values)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = iter(data.split())
        def deserializer():
            val = next(data)
            if val == "#":
                return None
            else:
                node = TreeNode(int(val))
                node.left = deserializer()
                node.right = deserializer()
                return node
        
        tree = deserializer()
        return tree
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

