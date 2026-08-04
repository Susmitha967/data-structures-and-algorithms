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
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()

            if node is None:
                res.append("#")
            else:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ",".join(res)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        node = data.split(",")
        root = TreeNode(int(node[0]))
        q = deque([root])
        i = 1
        while q:
            cur = q.popleft()
            if node[i] != '#':
                cur.left = TreeNode(int(node[i]))
                q.append(cur.left)
            i += 1

            if node[i] != '#':
                cur.right = TreeNode(int(node[i]))
                q.append(cur.right)
            i += 1
        return root 

        







































        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))