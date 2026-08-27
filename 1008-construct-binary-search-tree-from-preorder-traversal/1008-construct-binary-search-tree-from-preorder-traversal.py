# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.i = 0
    def construct(self,arr,m):
        if self.i == len(arr) or arr[self.i] > m:
            return None
        root = TreeNode(arr[self.i])
        self.i += 1
        root.left = self.construct(arr,root.val)
        root.right = self.construct(arr,m)
        return root
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        m = float('inf')
        return self.construct(preorder,m)