class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return not p and not q or p and q and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSameTree(root, subRoot) or root and (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
