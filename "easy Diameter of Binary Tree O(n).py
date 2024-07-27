def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
        if not root:
            return 0

        l, r = dfs(root.left), dfs(root.right)
        diameter[0] = max(diameter[0], l + r)

        return max(l, r) + 1

    diameter = [0]
    dfs(root)

    return diameter[0]
