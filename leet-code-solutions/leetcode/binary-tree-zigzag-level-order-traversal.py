# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # cur = root
        li = []
        dd = defaultdict(list)
        def tree(root, d):
            if not root:
                return 
     
            dd[d].append(root.val)

            tree(root.left,d+1)
            tree(root.right,d+1)
        tree(root, 0)
        for key, i in dd.items():
            if key % 2 == 0: 
                li.append(i)
            else:
                li.append(reversed(i))
        return li
            # print(li)
       

        


        