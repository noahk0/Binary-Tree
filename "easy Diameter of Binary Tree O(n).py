def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.diameter = 0
    
    def dfs(root):
        if not root:
            return 0

        l, r = dfs(root.left), dfs(root.right)
        self.diameter = max(self.diameter, l + r)

        return max(l, r) + 1

    dfs(root)

    return self.diameter
