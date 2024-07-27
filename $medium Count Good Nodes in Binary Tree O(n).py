def goodNodes(self, root: TreeNode) -> int:
    def dfs(node, great):
        count[0] += great <= node.val
        great = max(great, node.val)

        if node.left:
            dfs(node.left, great)

        if node.right:
            dfs(node.right, great)

    count = [0]

    dfs(root, root.val)

    return count[0]
