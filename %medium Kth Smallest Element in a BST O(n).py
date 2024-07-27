def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    dfs = []

    while dfs or root:
        while root:
            dfs.append(root)
            root = root.left

        k -= 1
        root = dfs.pop()

        if not k:
            return root.val

        root = root.right
