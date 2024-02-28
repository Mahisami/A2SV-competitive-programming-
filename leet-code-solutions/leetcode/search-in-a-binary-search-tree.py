# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        ans = []
        def tree(root,val):
            if not root:
                return None
            if root.val == val:
                return root
            if root.val > val:
                return tree(root.left, val)
            else:
                return tree(root.right, val)
        
        return tree(root,val)
         

    
            #     ans.append(tree(root.left))
            #     ans.append(tree(root.right))
            # if root.right == val:
            #     ans.append(root.left)

        