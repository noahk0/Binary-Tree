def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, great):
        nonlocal count

        count += great <= node.val
        great = max(great, node.val)

        if node.left:
            dfs(node.left, great)

        if node.right:
            dfs(node.right, great)

    count = 0

    dfs(root, root.val)

    return count
