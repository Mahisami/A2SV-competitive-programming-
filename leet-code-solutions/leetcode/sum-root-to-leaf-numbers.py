# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def tree(root,cursum):
            if not root:
                return 0
            cursum = cursum *10 + root.val
            if not root.left and not root.right:
                return cursum
            else:
                return tree(root.left, cursum)+ tree(root.right, cursum)


        return tree(root,0)


        
       
        