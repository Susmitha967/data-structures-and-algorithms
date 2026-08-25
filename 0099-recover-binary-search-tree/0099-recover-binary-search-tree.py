# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # first = last = None
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # if not root:
            # return
        self.f = self.l = self.m = None
        self.prev = TreeNode(float('-inf'))
        def recover(root):
            if not root:
                return
            recover(root.left)
            if root.val < self.prev.val:
                if self.f is None:
                    self.f = self.prev
                    self.m = root
                else:
                    self.l = root
            self.prev = root
            recover(root.right)

        recover(root)
        if self.f and self.l:
            self.f.val, self.l.val = self.l.val , self.f.val
        elif self.f and self.m:
            self.f.val , self.m.val = self.m.val , self.f.val
        