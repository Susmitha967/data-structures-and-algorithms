# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def valid(self,root,mini,maxi):
        if not root:
            return True
        if root.val <= mini or root.val >= maxi:
            return False
        return self.valid(root.left,mini,root.val) and self.valid(root.right,root.val,maxi)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = float('-inf')
        maxi = float('inf')
        return self.valid(root,mini,maxi)

        