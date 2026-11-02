# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        temp = root
        
        while temp!= None:
            if p.val>temp.val and q.val>temp.val:
                temp = temp.right
            elif p.val<temp.val and q.val<temp.val:
                temp = temp.left
            else:
                return temp
        