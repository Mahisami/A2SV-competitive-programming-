# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int: 
        # maxVal = 0 
        # minVal = float("inf")
        li = []
        def tree(root,maxVal,minVal):
            maxVal = max(root.val, maxVal)
            minVal = min(root.val, minVal)
            if not root.left and not root.right:
                li.append(maxVal - minVal)
                return 

            

            
            # li = maxVal - minVal
            if root.left:
                tree(root.left, maxVal,minVal)
            if root.right:
                tree(root.right,maxVal, minVal)
            
        tree(root,0,float("inf"))
        return max(li)
        