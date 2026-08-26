# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def convert(self,head):
        temp = head
        while temp:
            self.arr.append(temp.val)
            temp = temp.next
        # print(self.arr)
        return self.arr
    def intoBST(self,l,r,arr):
        if l > r:
            return
        mid = (l+r)//2
        root = TreeNode(arr[mid])
        root.left = self.intoBST(l,mid-1,arr)
        root.right = self.intoBST(mid+1,r,arr)
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.convert(head)
        # print(self.arr)
        return self.intoBST(0,len(self.arr)-1,self.arr)
        