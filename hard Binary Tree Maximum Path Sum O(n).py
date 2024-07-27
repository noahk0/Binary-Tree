def maxPathSum(self, root: Optional[TreeNode]) -> int:
    def dfs(node):
        left, right = max(dfs(node.left), 0) if node.left else 0, max(dfs(node.right), 0) if node.right else 0
        total[0] = max(total[0], node.val + left + right)

        return node.val + max(left, right)

    total = [root.val]

    dfs(root)

    return total[0]
