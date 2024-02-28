# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = []
        def tree(root):
            
            if root:
                tree(root.left)
                ans.append(root.val)
                tree(root.right)
        
        tree(root)
        # res = all(i < j for i, j in zip(ans, ans[1:]))
        return ans[k-1]


        