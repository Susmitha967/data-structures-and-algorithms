# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def build(self,ps,pe,ins,ine,inorder,preorder):
        hm = {val:ind for ind,val in enumerate(inorder)}
        if ins > ine or ps > pe:
            return None
        root_val = preorder[ps]
        root = TreeNode(root_val)
 
        inroot = hm[root_val]
        nodeleft = inroot-ins

        root.left = self.build(ps+1,ps+nodeleft+1,ins,inroot-1,inorder,preorder) 
        root.right = self.build(ps+nodeleft+1,pe,inroot+1,ine,inorder,preorder)
        return root

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        return self.build(0,len(preorder)-1,0,len(inorder)-1,inorder,preorder)
        