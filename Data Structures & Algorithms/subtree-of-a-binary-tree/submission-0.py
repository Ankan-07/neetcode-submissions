# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        if root is None and subRoot is None:
            return True
        
        if self.isSameTree(root,subRoot):
            return True
        
        left = self.isSubtree(root.left,subRoot)
        right = self.isSubtree(root.right,subRoot)

        if left or right:
            return True
        else:
            return False

    def isSameTree(self,node1:Optional[TreeNode],node2:Optional[TreeNode])->bool:
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        if node1.val != node2.val:
            return False
        l = self.isSameTree(node1.left,node2.left)
        r = self.isSameTree(node1.right,node2.right)
        return (l and r)