def maxPathSum(self, root: Optional[TreeNode]) -> int:
    def dfs(node):
        left, right = max(dfs(node.left), 0) if node.left else 0, max(dfs(node.right), 0) if node.right else 0
        self.total = max(self.total, node.val + left + right)

        return node.val + max(left, right)

    self.total = root.val

    dfs(root)

    return self.total
