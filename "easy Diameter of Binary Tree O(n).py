def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root:
            return 0

        nonlocal diameter

        l, r = dfs(root.left), dfs(root.right)
        diameter = max(diameter, l + r)

        return max(l, r) + 1

    diameter = 0
    dfs(root)

    return diameter
