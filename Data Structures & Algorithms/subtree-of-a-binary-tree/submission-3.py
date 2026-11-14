# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # if not root and not subRoot: return True
        # if not root or not subRoot: return False

        stack = []
        while stack or root:
            while(root):
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val == subRoot.val and self.isSameTree(root, subRoot): 
                return True
            root = root.right
        return False
        
