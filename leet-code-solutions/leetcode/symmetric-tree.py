# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def tree(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            # if tree(root.left) == tree(root.right):
            #     return True

            return (left.val == right.val) and tree(left.left, right.right) and tree(left.right, right.left)
                   

        # if not root:
        #     return True  

        return tree(root.left, root.right)

        