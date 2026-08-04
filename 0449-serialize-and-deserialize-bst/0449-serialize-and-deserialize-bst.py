# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ""
        res = []
        q = deque([root])
        while q:
            nodes = q.popleft()
            if nodes is None:
                res.append("#")
            else:
                res.append(str(nodes.val))
                q.append(nodes.left)
                q.append(nodes.right)
        return ",".join(res)
        
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()

            if nodes[i] != "#":
                cur.left = TreeNode(int(nodes[i]))
                q.append(cur.left)
            i +=1
            if nodes[i] != "#":
                cur.right = TreeNode(int(nodes[i]))
                q.append(cur.right)
            i += 1
        return root 

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))