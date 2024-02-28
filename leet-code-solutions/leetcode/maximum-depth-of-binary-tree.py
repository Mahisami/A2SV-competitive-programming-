# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
            
        def tree(x):
            if not x:
                return 0
            leftdepth = tree(x.left)
            rightdepth = tree(x.right)

            return max(leftdepth, rightdepth) + 1
        return tree(root)
        