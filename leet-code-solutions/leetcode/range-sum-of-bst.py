# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def tree(root):
            if not root:
                return 0

            cur = 0
            if low <= root.val <= high:
                cur = root.val
            left = tree(root.left)
            right = tree(root.right)

            return cur + left + right
        return tree(root)
