def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def dfs(node, low, high):
        return low < node.val < high and (not node.left or dfs(node.left, low, node.val)) and (not node.right or dfs(node.right, node.val, high))

    return dfs(root, float('-inf'), float('inf'))
