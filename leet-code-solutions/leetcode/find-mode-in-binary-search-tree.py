# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        # print(root.val.count())
        def tree(root):
           
                
            if root:
                d[root.val] += 1
                tree(root.left)
                tree(root.right)
              
        d = defaultdict(int)
        arr = []
        tree(root) 
        maxv = max(d.values())
        for i in d.keys():
            if maxv == d[i]:
                arr.append(i)
        return arr



    






















      