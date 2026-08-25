# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convert(self,l,r,nums):
        if l > r:
            return
        mid = (l+r)//2
        root = TreeNode(nums[mid])
        root.left = self.convert(l,mid-1,nums)
        root.right = self.convert(mid+1,r,nums)
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.convert(0,len(nums)-1,nums)
        
        # root.right = self.sortedArrayToBST(nums[mid:])
        # return root