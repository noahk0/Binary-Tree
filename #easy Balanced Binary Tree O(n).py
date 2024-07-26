def isBalanced(self, root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    l, r = int(self.isBalanced(root.left)), int(self.isBalanced(root.right))

    if not l or not r or 1 < abs(l - r):
        return False

    return max(l, r) + 1
