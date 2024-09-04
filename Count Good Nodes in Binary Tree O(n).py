def goodNodes(self, root: TreeNode) -> int:
    self.count = 0
    
    def dfs(node, great):
        self.count += great <= node.val
        great = max(great, node.val)

        if node.left:
            dfs(node.left, great)

        if node.right:
            dfs(node.right, great)

    dfs(root, root.val)

    return self.count
