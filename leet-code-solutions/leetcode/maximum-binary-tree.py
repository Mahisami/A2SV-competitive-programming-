# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        # maxVal = 0
        if not nums:
            return None
            
        maxVal = max(nums)
        maxIndex = nums.index(maxVal)
        # print(maxIndex)
        root = TreeNode( maxVal)
        root.left= self.constructMaximumBinaryTree(nums[:maxIndex])
        root.right = self.constructMaximumBinaryTree(nums[maxIndex + 1:])
        
            
        return root
        