# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if not root:
            return 0
        q = deque()
        q.append([root,0])
        while q:
            min_ind = q[0][1]
            size = len(q)
            first = last = 0
            for i in range(size):
                node, ind = q.popleft()
                curr_ind = ind - min_ind
                if i == 0:
                    first = curr_ind
                if i == size-1:
                    last = curr_ind
                if node.left:
                    q.append((node.left,2*curr_ind+1))
                if node.right:
                    q.append((node.right,2*curr_ind+2))
            ans = max(ans, last-first+1) 
        return ans

        