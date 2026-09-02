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
        q = deque()
        q.append(root)
        s = []
        while q:
            cur = q.popleft()
            if cur is None:
                s.append("#")
            else:
                s.append(str(cur.val))
                q.append(cur.left)
                q.append(cur.right)
        return ",".join(s)
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        s = data.split(",")
        root = TreeNode(int(s[0]))
        i = 1
        q = deque([root])
        # q.append([root])
        while q:
            cur = q.popleft()
            if s[i] != "#":
                cur.left = TreeNode(int(s[i]))
                q.append(cur.left)
            i += 1
            if s[i] != '#':
                cur.right = TreeNode(int(s[i]))
                q.append(cur.right)
            i += 1
        return root
       






































        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))