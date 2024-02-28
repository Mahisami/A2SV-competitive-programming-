# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def tree(root):
            
            if root:
                tree(root.left)
                arr.append(root.val)
                tree(root.right)
            # return arr
           

        # arr = []
        tree(root)
        res = all(i < j for i, j in zip(arr, arr[1:]))
        return res