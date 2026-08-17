# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sum = 0
    def sumTree(self,root):
        if not root:
            return
        self.sumTree(root.right)
        self.sum += root.val
        root.val = self.sum
        self.sumTree(root.left)
        return root
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.sumTree(root)