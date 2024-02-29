# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mycmp(self,a, b): 
        if a[0] > b[0]: 
            return 1
        elif a[0] == b[0]:
            if a[1] > b[1]:
                return 1
            elif a[1] < b[1]:
                return -1
            else:
                return 0
        elif a[0] < b[0]: 
            return -1
        else: 
            return 0

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dd = defaultdict(list)
        li = []

        def tree(root, d, p):
            if not root:
                return 
            dd[p].append([d, root.val])
            tree(root.left,d+1,p-1)
            tree(root.right, d+1, p+1)
         
            
        tree(root, 0,0)
        for key, i in sorted(dd.items()):
            i.sort(key = cmp_to_key(self.mycmp))
            li.append([i[j][1] for j in range(len(i))])
        return li        